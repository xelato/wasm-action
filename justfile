# show commands
default:
    just --list

# https://raw.githubusercontent.com/bytecodealliance/registry/refs/heads/main/crates/server/openapi.yaml

# generate warg client
generate-warg-openapi:
    rm -rf warg_openapi
    container run --rm -v "${PWD}:/local" \
        openapitools/openapi-generator-cli generate \
        -i /local/openapi/warg.yml \
        -g python-pydantic-v1 \
        -o /local/warg-openapi \
        --package-name warg_openapi \
        --http-user-agent xelato-wasm-action
    mv warg-openapi/warg_openapi .
    rm -rf warg-openapi

# validate openAPI definition
validate:
    docker run --rm -v "${PWD}:/local" \
        openapitools/openapi-generator-cli validate \
        -i /local/openapi/warg.yml

generate-warg-proto:
    mkdir -p warg_proto
    protoc --python_out warg_proto proto/warg/protocol/warg.proto
    mv warg_proto/proto/warg/protocol/warg_pb2.py warg_proto.py
    rm -rf warg_proto

pytest:
    uv run --with pytest pytest test_*.py

# ngrok-proxy to wa.dev
ngrok:
    ngrok http \
        --url=$NGROK_DOMAIN \
        https://warg.wa.dev/ --host-header warg.wa.dev \
        --request-header-remove X-Forwarded-For \
        --request-header-remove X-Forwarded-Host \
        --request-header-remove X-Forwarded-Proto \

# test warg-pull
test-warg-pull:
    uv run action.py warg-pull \
        --registry wa.dev \
        --warg-url https://$NGROK_DOMAIN/ \
        --namespace component-book \
        --name adder \
