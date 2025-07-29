# show commands
default:
    just --list

# https://raw.githubusercontent.com/bytecodealliance/registry/refs/heads/main/crates/server/openapi.yaml

# generate warg client
generate-warg-client:
    container run --rm -v "${PWD}:/local" \
        openapitools/openapi-generator-cli generate \
        -i /local/openapi/warg.yml \
        -g python-pydantic-v1 \
        -o /local/warg-openapi \
        --package-name warg_openapi \
        --http-user-agent xelato-wasm-action \


validate:
    container run --rm -v "${PWD}:/local" \
        openapitools/openapi-generator-cli validate \
        -i /local/openapi/warg.yml
