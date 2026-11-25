
import os
import anthropic

# 1. 读取环境变量
api_key = os.environ.get("DEEPSEEK_API_KEY")
model = os.environ.get("LLM_MODEL", "deepseek-flash")

if not api_key:
    raise RuntimeError("没有找到 DEEPSEEK_API_KEY，请检查 .env")

# 2. 创建 DeepSeek 客户端
client = anthropic.Anthropic(
    api_key=api_key,
    base_url="https://api.deepseek.com/anthropic",
)

# 3. 发送请求
print("正在请求 DeepSeek API...")

response = client.messages.create(
    model=model,
    max_tokens=256,
    messages=[
        {
            "role": "user",
            "content": "你好！请用中文介绍一下你自己，以及你能帮助我完成哪些 AI 开发任务。"
        }
    ],
)

# 4. 输出结果
print("\n========== DeepSeek API 响应 ==========")

for block in response.content:
    if block.type == "text":
        print(block.text)

print("\n========== 请求信息 ==========")
print("模型:", response.model)
print("输入 Token:", response.usage.input_tokens)
print("输出 Token:", response.usage.output_tokens)

print("\nDeepSeek API 调用成功！")
