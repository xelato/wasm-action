<div align="center">
  <a href="https://pypi.python.org/pypi/wasm-action"><img src="https://img.shields.io/pypi/v/wasm-action.svg" alt="PyPI"></a>
  <a href="https://github.com/xelato/wasm-action/blob/main/LICENSE"><img src="https://img.shields.io/github/license/xelato/wasm-action.svg?v=2" alt="license"></a>
</div>

# wasm-action

**Wasm-action facilitates the creation, distribution and generic utilization of non-browser based WebAssembly workloads through a local-first approach with a focus on privacy and security. Written primarily in Python, it also explores the Python ecosystem's maturity for WebAssembly and beyond.**

## Features
* Versatile use as GitHub [action](https://github.com/marketplace/actions/wasm-action), CLI or Python [library](https://pypi.org/project/wasm-action/).
* Supported registry types: warg (wa.dev)
* Supported artifact types: wasm
* Supported actions: push, pull
* Supports Python 3.10+ on Linux, MacOS and Windows
* Python sandbox using wasm build of cpython 3.14

#### Planned
* OCI registry support (a.k.a. Docker registry)
* Convert between formats (wit/wasm)

## Usage
### Pull from registry
```
      - uses: xelato/wasm-action@main
        with:
          action: pull
          registry: wa.dev
          package: component-book:adder
```

To pull a private package, define your [token](https://wa.dev/account/credentials/new):
```
        env:
          WARG_TOKEN: ${{ secrets.WARG_TOKEN }}
```

<details>
<summary>Inputs</summary>

| Name | Description | Required | Example |
|------|-------------|----------|---------|
|action|Pull from registry|yes|pull|
|registry|Registry domain name|yes|wa.dev|
|package|Package specification|yes|namespace:name@version<br>namespace:name<br>namespace/name<br>namespace/name@version|
|path|Target path to save the download|no|file.wasm|

</details>

<details>
<summary>Outputs</summary>

| Name | Description | Example |
|------|-------------|---------|
|registry|Registry domain name|wa.dev|
|registry-type|Detected registry type|warg|
|package|Package|foo:bar@1.2.3|
|package-namespace|Package namespace|foo|
|package-name|Package name|bar|
|package-version|Package version|1.2.3|
|filename|Download location|foo-bar_1.2.3.wasm|
|digest|File hash|sha256:2afffac0...|

</details>

### Push to registry
```
      - uses: xelato/wasm-action@main
        with:
          action: push
          registry: wa.dev
          package: foo:bar@1.2.3
          path: files/foo_bar_1.2.3.wasm
        env:
          WARG_TOKEN: ${{ secrets.WARG_TOKEN }}
          WARG_PRIVATE_KEY: ${{ secrets.WARG_PRIVATE_KEY }}
```

## CLI
The tool can be run without installing, using [uv/uvx](https://docs.astral.sh/uv/).
```
$ uvx wasm-action --help          
Usage: wasm-action [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  eval     Expression evaluator
  key      Generate private key or read one from stdin
  pull     Pull from registry
  push     Push to registry
  python   Python in a sandbox
  version  Print version
  x        Run a WebAssembly file
```
<details>
<summary><b>Pull from registry</b></summary>

```
$ uvx wasm-action pull --registry wa.dev --package wasi:io
registry=wa.dev
registry-type=warg
warg-url=https://warg.wa.dev
package=wasi:io@0.2.0
package-namespace=wasi
package-name=io
package-version=0.2.0
digest=sha256:c33b1dbf050f64229ff4decbf9a3d3420e0643a86f5f0cea29f81054820020a6
filename=wasi:io@0.2.0.wasm
```
```
$ file wasi:io@0.2.0.wasm 
wasi:io@0.2.0.wasm: WebAssembly (wasm) binary module version 0x1000d
```

</details>

<details>
<summary><b>Push to registry</b></summary>

```
$ export WARG_TOKEN="..."
$ export WARG_PRIVATE_KEY="..."
$ uvx wasm-action push -r wa.dev -p foo:bar@1.2.3 --path foo_bar_1.2.3.wasm
```
      
</details>

<details open>
<summary><b>Key generation</b></summary>

New [token](https://wa.dev/account/credentials/new) registration and push to wa.dev require generation and configuration of a private/public key pair which can be facilitated with:
```
$ uvx wasm-action key
{
    "private": "ecdsa-p256:9y5nigLvFp3KZZQtuvN9DchpGIMUB4bwGAtkIoOCla4=",
    "public": "ecdsa-p256:AvspSQWBK65ItTou/uVCi5qC4P+HBCi4R34OIPb3ILRl",
    "id": "sha256:c836bd8a3082f2e8d70bdfa48296e580ab847fcdeadb351f448d03f152d44093"
}
```
```
# use private key to configure in github or save it elsewhere in a secure manner
$ uvx wasm-action key | jq .private | pbcopy
```
```
# use corresponding public key for new token registration at wa.dev
$ pbpaste | uvx wasm-action key | jq .public
```

</details>

## Use as Library
The package is [published](http://pypi.org/project/wasm-action/) to the Python Package Index and can be installed/depended-on under the name `wasm-action` on all [supported](https://devguide.python.org/versions/#versions) Python versions.
```
$ pip install wasm-action
```
```
>>> import wasm_action as wa
>>> wa.pull('wa.dev', 'wasi:io')
PackageDownload(namespace='wasi', name='io', version='0.2.0', content='...', digest='sha256:c33b1dbf050f64229ff4decbf9a3d3420e0643a86f5f0cea29f81054820020a6')
```
However, the library interface is not yet standardised and may (and will!) change.

## Python Sandbox
Experimental support for running a [WASI](https://github.com/WebAssembly/WASI) build of python/cpython@3.14.

```
$ uvx --python 3.14 wasm-action python --version
Python 3.14.2+
```

The characters `--` can be used to separate host from guest options in cases where there's ambiguity:
```
# get guest interpreter help
$ uvx --python 3.14 wasm-action python -- --help
```

### Host Python
The Python interpreter used to run `wasm-action`. It orchestrates and mediates the guest Python execution under a supported WebAssembly Runtime ([wasmtime](https://wasmtime.dev)).

### Guest Python
The Python interpreter that was compiled to WebAssembly. Guest Python runs in a restricted "sandbox" environment. In addition to the .wasm module file, it also requires the Python standard library folder, currently being reused from the host Python installation.

#### Interpreter
Currently there is a choice between `--interpreter cpython` (default) and `--interpreter monty`.

#### Layout
Guest code has access to the following paths:

* / - host's current working directory (read/write)
* /usr/local/lib/python3.14 - host Python's stdlib (read only)
* /tmp (read/write)

#### Environment variables
Code running in the guest environment only has access to the environment variables explicitly defined:
```
>>> import os
>>> os.environ
environ({'PYTHONPATH': '/usr/local/lib/python3.14:/build'})
```
Additional variables can be defined with the `-e/--env` option.

#### Packages
#### Limitations

### Application
Running [untrusted](https://github.com/xelato/wasm-action/tree/main/example) code, such as one generated by an LLM.
