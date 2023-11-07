#!/bin/bash

GENERATOR_VERSION=v7.0.1

docker run --rm \
    -v $PWD:/local openapitools/openapi-generator-cli:$GENERATOR_VERSION generate \
    -g python \
    -c /local/python-config.yaml \
    -i /local/openapi.yaml \
    -o /local/python

# reset ownership
sudo chown $USER:$USER -R *
