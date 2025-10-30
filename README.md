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
      - name: Pull from registry
        uses: xelato/wasm-action
        id: pull
        with:
          action: pull
          registry: wa.dev
          namespace: component-book
          name: adder
```

Outputs:
```
      - name: Display outputs
        shell: bash
        run: |
          echo "registry:" ${{ steps.pull.outputs.registry }}
          echo "registry-type:" ${{ steps.pull.outputs.registry-type }}
          echo "namespace:" ${{ steps.pull.outputs.namespace }}
          echo "name:" ${{ steps.pull.outputs.name }}
          echo "version:" ${{ steps.pull.outputs.version }}
          echo "filename:" ${{ steps.pull.outputs.filename }}
          echo "digest:" ${{ steps.pull.outputs.digest }}
```
