
import os
import anthropic

# 创建 DeepSeek 客户端
client = anthropic.Anthropic(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com/anthropic"
)

# 选择模型
MODEL = os.environ.get(
    "DEEPSEEK_MODEL",
    "deepseek-flash"
)

# 发送请求
response = client.messages.create(
    model=MODEL,
    max_tokens=256,
    thinking={"type": "disabled"},
    messages=[
        {
            "role": "user",
            "content": "我上一个提问的是什么？"
        }
    ]
)

# 输出回答
print("DeepSeek 回答：")

for block in response.content:
    if block.type == "text":
        print(block.text)

# 输出 Token 使用量
print("\nToken 使用情况：")
print("Input:", response.usage.input_tokens)
print("Output:", response.usage.output_tokens)

print(response)
