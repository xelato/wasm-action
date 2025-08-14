# show commands
default:
    just --list

# https://raw.githubusercontent.com/bytecodealliance/registry/refs/heads/main/crates/server/openapi.yaml

# generate warg client
generate-warg-client:
    rm -rf warg-openapi
    container run --rm -v "${PWD}:/local" \
        openapitools/openapi-generator-cli generate \
        -i /local/openapi/warg.yml \
        -g python-pydantic-v1 \
        -o /local/warg-openapi \
        --package-name warg_openapi \
        --http-user-agent xelato-wasm-action \


# validate openAPI definition
validate:
    container run --rm -v "${PWD}:/local" \
        openapitools/openapi-generator-cli validate \
        -i /local/openapi/warg.yml

# test warg-push
test-warg-push:
    uv run action.py warg-push \
        --warg-url https://warg.wa.dev/ \
        --filename test/files/gcd@0.0.1.wasm \
        --namespace rocketniko \
        --name gcd \
        --version 0.0.1 \
