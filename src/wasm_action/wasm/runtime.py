
import os
import wasmtime


def module_file(filename):
    if not os.path.exists(filename) or not os.path.isfile(filename):
        raise Exception('file not found: {}'.format(filename))

    with open(filename, 'rb') as f:
        module_bytes = f.read()
    return module(module_bytes)


def module(module_bytes):
    return Module(module_bytes)


class Module:

    def __init__(self, module_bytes):
        self._store = wasmtime.Store()
        self._module = wasmtime.Module(self._store.engine, module_bytes)

    def instance(self):
        return Instance(store=self._store, module=self._module)


class Instance:

    def __init__(self, store, module):
        self._store = store
        self._module = module
        self._instance = None
        self._imports = []

    def function(self, name):
        if not self._instance:
            self._instance = wasmtime.Instance(self._store, self._module, self._imports)
        exports = self._instance.exports(self._store)
        if name not in exports.keys():
            print('defined functions:', tuple(exports.keys()))
            assert False, "function not found: {}".format(name)
        return Function(store=self._store, func=exports[name])


class Function:

    _types = {
        "i32": int,
        "i64": int,
        "f32": float,
        "f64": float,
    }

    def __init__(self, store, func):
        self._store = store
        self._func = func
        self._func_type = self._func.type(self._store)

    def call(self, *args):
        # convert to expected types before function call
        typed_args = []
        for param, arg in zip(self._func_type.params, args):
            type = self._types.get(str(param))
            arg = type(arg) if type else arg
            typed_args.append(arg)
        return self._func(self._store, *typed_args)
