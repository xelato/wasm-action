# show commands
default:
    just --list

# https://raw.githubusercontent.com/bytecodealliance/registry/refs/heads/main/crates/server/openapi.yaml

# generate warg client
openapi-generate:
    rm -rf src/warg_openapi
    container run --rm -v "${PWD}:/local" \
        openapitools/openapi-generator-cli generate \
        -i /local/openapi/warg.yml \
        -g python-pydantic-v1 \
        -o /local/warg-openapi \
        -p useOneOfDiscriminatorLookup=true \
        --package-name warg_openapi \
        --http-user-agent xelato-wasm-action
    mv warg-openapi/warg_openapi src
    rm -rf warg-openapi

# validate openAPI definition
openapi-validate:
    docker run --rm -v "${PWD}:/local" \
        openapitools/openapi-generator-cli validate \
        -i /local/openapi/warg.yml

# generate protobuf module
proto:
    mkdir -p warg_proto
    protoc --python_out warg_proto proto/warg/protocol/warg.proto
    mv warg_proto/proto/warg/protocol/warg_pb2.py src/wasm_action/warg/proto.py
    rm -rf warg_proto

# test
pytest:
    PYTHONPATH=. uv run --with pytest pytest

ngrok:
    ngrok http \
        --url=$NGROK_DOMAIN \
        https://warg.wa.dev/ --host-header warg.wa.dev \
        --request-header-remove X-Forwarded-For \
        --request-header-remove X-Forwarded-Host \
        --request-header-remove X-Forwarded-Proto \

clean:
    rm -rf .venv
    rm -rf .pytest_cache
    rm -rf .ruff_cache
    find . -name "__pycache__" | xargs -n1 rm -rf
    rm -rf dist


check:
    uvx ruff format
    uvx ruff check
