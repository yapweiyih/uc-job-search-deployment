#!/usr/bin/env bash

# This is for awscli v2
aws lambda invoke \
    --cli-binary-format raw-in-base64-out \
    --function-name sam-app-GetEmbeddingFunc-UX62MVS162XW \
    --invocation-type RequestResponse \
    --payload '{"body": {"sentence": ["this is a test", "this is another test"]}}' \
    response.json


# Using Alias
aws lambda invoke \
    --cli-binary-format raw-in-base64-out \
    --function-name sam-app-GetEmbeddingFunc-UX62MVS162XW:v1 \
    --invocation-type RequestResponse \
    --payload '{"body": {"sentence": ["this is a test", "this is another test"]}}' \
    response.json