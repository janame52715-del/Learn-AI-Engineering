import os
import urllib.request
import json
import urllib.error

url = "https://api.deepseek.com/anthropic/v1/messages"

headers = {
        "Content-Type": "application/json",
        "x-api-key": os.environ["DEEPSEEK_API_KEY"],
        "anthropic-version": "2023-06-01",
        }

body = json.dumps({
    "model": os.environ.get("DEEPSEEK_MODEL","deepseek-flash"),
    "max_tokens": 256,
    "messages": [
        {
            "role": "user",
            "content": "who are you?"
            }
        ],
    }).encode()

req = urllib.request.Request(
        url,
        data=body,
        headers=headers,
        method="POST"
        )

with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    for block in result.get("content",[]):
        if block.get("type") == "text":
            print(block.get("text"))

print(result)
