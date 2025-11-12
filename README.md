# wasm-action

**Interact with WebAssembly registries.**

## Features
* Versatile use as a GitHub [action](https://github.com/marketplace/actions/wasm-action), CLI or Python [library](https://pypi.org/project/wasm-action/).
* Supported registry types: warg (wa.dev)
* Supported artifact types: wasm
* Supported actions: pull
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
|digest|File hash|sha256:2afffac0a89b4f6add89903754bb5a09a51378ef14f159283c1a6408abb43147|
