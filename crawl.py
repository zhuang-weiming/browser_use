from langchain_google_genai import ChatGoogleGenerativeAI # 修改导入
from browser_use import Agent
import asyncio # 导入 asyncio
from dotenv import load_dotenv
import os # 新增导入

# 使用绝对路径加载 .env 文件
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
print(f"环境变量: GEMINI_API_KEY={os.getenv('GEMINI_API_KEY')}, GOOGLE_API_KEY={os.getenv('GOOGLE_API_KEY')}")

# 设置多个可能的环境变量名称
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("未找到 GEMINI_API_KEY 或 GOOGLE_API_KEY 环境变量")

# 设置环境变量
os.environ["GOOGLE_API_KEY"] = api_key

# 使用 LangChain 模型
llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',  # 使用更稳定的模型版本
    google_api_key=api_key,  # 显式传递 API 密钥
    temperature=0.7
)

# Create agent with the model
agent = Agent(
    task="Please compare the price of cloud service of AWS and GCP",
    llm=llm
)

async def main(): # 定义一个异步函数
    result = await agent.run()       # 使用 await 调用 run 方法
    print(result)

if __name__ == "__main__":
    asyncio.run(main()) # 运行异步函数
