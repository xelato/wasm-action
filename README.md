# wasm-action

**Interact with WebAssembly registries.**

## Features
* Versatile use as GitHub [action](https://github.com/marketplace/actions/wasm-action), CLI or Python [library](https://pypi.org/project/wasm-action/).
* Supported registry types: warg (wa.dev)
* Supported artifact types: wasm
* Supported actions: push, pull
* Supports Python 3.10+ on Linux, MacOS and Windows

## Usage
### Pull from registry
```
      - uses: xelato/wasm-action
        with:
          action: pull
          registry: wa.dev
          package: component-book:adder
```

To pull a private package define your [token](https://wa.dev/account/credentials/new):
```
        env:
          WARG_TOKEN: ${{ secrets.WARG_TOKEN }}
```

#### Inputs

| Name | Description | Required | Example |
|------|-------------|----------|---------|
|action|Pull from registry|yes|pull|
|registry|Registry domain name|yes|wa.dev|
|package|Package specification|yes|namespace:name@version<br>namespace:name<br>namespace/name<br>namespace/name@version|
|path|Target path to save the download|no|file.wasm|

#### Outputs:
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

### Push to registry
```
      - uses: xelato/wasm-action
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
The tool can be run without installing using [uv](https://docs.astral.sh/uv/).
```
$ uvx wasm-action --help
Usage: wasm-action [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  pull  Pull from a WebAssembly registry
  push  Push to a WebAssembly registry
```
```
$ uvx wasm-action pull --help
Usage: wasm-action pull [OPTIONS]

  Pull from a WebAssembly registry

Options:
  --registry TEXT    registry domain name  [required]
  --package TEXT     package spec  [required]
  --path TEXT        filename
  --warg-token TEXT  warg token
  --help             Show this message and exit.
```
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
