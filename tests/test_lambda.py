import json
import time

import boto3

"""
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

func_name = "embedding-GetEmbeddingFunc-HE1UG2AXZ076:1"

response = lambda_client.invoke(
    FunctionName=func_name,
    InvocationType="RequestResponse",
    LogType="Tail",
    Payload=json.dumps(payload),
    # Qualifier='1',
)

result = response["Payload"].read()
print(result)
