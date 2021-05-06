#!/usr/bin/env bash

# Calling version:1
aws lambda invoke \
    --cli-binary-format raw-in-base64-out \
    --function-name embedding1-GetEmbeddingFunc-QB7126FHR1LR:TEST \
    --invocation-type RequestResponse \
    --payload '{"body": {"sentence": ["this is a test", "this is another test"]}}' \
    response.json