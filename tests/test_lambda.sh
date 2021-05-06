#!/usr/bin/env bash

# Calling LATEST
aws lambda invoke \
    --cli-binary-format raw-in-base64-out \
    --function-name embedding-GetEmbeddingFunc-HE1UG2AXZ076 \
    --invocation-type RequestResponse \
    --payload '{"body": {"sentence": ["this is a test", "this is another test"]}}' \
    response.json


# Calling version:1
aws lambda invoke \
    --cli-binary-format raw-in-base64-out \
    --function-name embedding-GetEmbeddingFunc-HE1UG2AXZ076:1 \
    --invocation-type RequestResponse \
    --payload '{"body": {"sentence": ["this is a test", "this is another test"]}}' \
    response.json