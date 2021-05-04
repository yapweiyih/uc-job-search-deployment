#!/usr/bin/env bash

# This is for awscli v2
aws lambda invoke \
    --cli-binary-format raw-in-base64-out \
    --function-name sam-app-HelloWorldFunction-18WRO6Q1F91IU \
    --invocation-type RequestResponse \
    --payload '{"body": {"sentence": ["this is a test", "this is another test"]}}' \
    response.json