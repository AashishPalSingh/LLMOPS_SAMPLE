import os
import json
import sys
import logging
import boto3

MODEL_ID = "meta.llama3-8b-instruct-v1:0"

prompt = """
You are a helpful assistant. So please let me know what is the capital of France?          
"""


bedrock = boto3.client(service_name="bedrock-runtime", region_name="ap-south-1")
payload = {
    "prompt": "[INST]" + prompt + "[/INST]",
    "max_gen_len": 512,
    "temperature": 0.3,
    "top_p": 0.9,
}

boday = json.dumps(payload)
model_id = MODEL_ID
response = bedrock.invoke_model(
    body=boday,
    modelId=model_id,
    contentType="application/json",
    accept="application/json",
)
response_body = response["body"].read().decode("utf-8")
response_json = json.loads(response_body)
print(response_json["generation"])
