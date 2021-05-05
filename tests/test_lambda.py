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

func_name = "sam-app-GetEmbeddingFunc-UX62MVS162XW:v1"


for i in range(300):
    response = lambda_client.invoke(
        FunctionName=func_name,
        InvocationType="RequestResponse",
        LogType="Tail",
        Payload=json.dumps(payload),
        # Qualifier='1',
    )
    print(i)
    time.sleep(1)

time.sleep(300)


result = response["Payload"].read()
print(result)
