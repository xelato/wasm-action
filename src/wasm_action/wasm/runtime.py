import os
import wasmtime

from . import expression


def module_file(filename):
    if not os.path.exists(filename) or not os.path.isfile(filename):
        raise Exception("file not found: {}".format(filename))

    with open(filename, "rb") as f:
        module_bytes = f.read()
    return module(module_bytes)


def module(module_bytes):
    return Module(module_bytes)


class Module:
    def __init__(self, module_bytes):
        self._store = wasmtime.Store()
        self._module = wasmtime.Module(self._store.engine, module_bytes)

    def wasi(self):
        return WASI(store=self._store, module=self._module)

    def instance(self):
        return Instance(store=self._store, module=self._module)


class Instance:
    def __init__(self, store, module, instance=None):
        self._store = store
        self._module = module
        if instance:
            assert isinstance(instance, wasmtime.Instance)
        self._instance = instance
        self._imports = []

    def __getattr__(self, name):
        """Ususally called by the evaluator to resolve function names."""
        return self.function(name)

    def function(self, name):
        if not self._instance:
            self._instance = wasmtime.Instance(self._store, self._module, self._imports)
        exports = self._instance.exports(self._store)
        if name not in exports.keys():
            print("defined functions:", list(exports.keys()))
            assert False, "function not found: {}".format(name)
        return Function(store=self._store, func=exports[name], name=name)

    def evaluate(self, text):
        """Evaluate an expression against functions exported in the instance."""
        return expression.evaluate(text or "", obj=self)


class WASI:
    def __init__(self, store, module):
        self._store = store
        self._module = module

        self.linker = wasmtime.Linker(self._store.engine)
        self.linker.define_wasi()

        self._wasi = wasmtime.WasiConfig()
        self._wasi.inherit_stdin()
        self._wasi.inherit_stdout()
        self._wasi.inherit_stderr()

        self._environ = {}

    def mount(self, host_path, guest_path, readonly=True):
        """Bind mount `host_path` as `guest_path` in the WASM instance."""
        self._wasi.preopen_dir(
            host_path,
            guest_path,
            dir_perms=wasmtime.DirPerms.READ_ONLY
            if readonly
            else wasmtime.DirPerms.READ_WRITE,
            file_perms=wasmtime.FilePerms.READ_ONLY
            if readonly
            else wasmtime.FilePerms.READ_WRITE,
        )
        return self

    def argv(self, argv):
        self._wasi.argv = argv
        return self

    def env(self, key, value):
        """Configure an environment variable in the WASM instance"""
        self._environ[key] = value
        return self

    def instance(self):
        self._wasi.env = [(k, v) for (k, v) in self._environ.items()]
        self._store.set_wasi(self._wasi)
        instance = self.linker.instantiate(self._store, self._module)
        return Instance(store=self._store, module=self._module, instance=instance)


class Function:
    _types = {
        "i32": int,
        "i64": int,
        "f32": float,
        "f64": float,
    }

    def __init__(self, store, func, name):
        self._store = store
        self._func = func
        self._func_type = self._func.type(self._store)
        self.name = name

    def call(self, *args):
        return self(*args)

    def __call__(self, *args):
        # convert to expected types before function call
        typed_args = []
        for param, arg in zip(self._func_type.params, args):
            type = self._types.get(str(param))
            arg = type(arg) if type else arg
            typed_args.append(arg)
        try:
            result = self._func(self._store, *typed_args)
        except Exception as e:
            message = "Error calling {}({}): {}".format(
                self.name,
                ", ".join([str(x) for x in typed_args]),
                str(e),
            )
            raise Exception(message)
        return result

    def __str__(self):
        return "{}({})".format(
            self.name, ", ".join([str(p) for p in self._func_type.params])
        )
