import json
import time

import boto3

"""
https://boto3.amazonaws.com/v1/documentation/api/1.9.42/reference/services/lambda.html#Lambda.Client.invoke

lambda_client.invoke(
    FunctionName="myfunctionname",
    InvocationType="Event" | "RequestResponse" | "DryRun",
    LogType="None" | "Tail",
    ClientContext="string",
    Payload=b"bytes" | file,
    Qualifier="string",
)
"""

lambda_client = boto3.client("lambda")
payload = {"body": {"sentence": ["this is a test", "this is another test"]}}
print(payload)
print(json.dumps(payload))

func_name = "embedding1-GetEmbeddingFunc-QB7126FHR1LR:TEST"

response = lambda_client.invoke(
    FunctionName=func_name,
    InvocationType="RequestResponse",
    LogType="Tail",
    Payload=json.dumps(payload),
)

result = response["Payload"].read()
print(result)
