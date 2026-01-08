import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage

# LLM implementations
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

from src.agent.tools import plot_ramachandran_tool


# -------------------------
# Load environment variables
# -------------------------
load_dotenv()


def build_llm():
    provider = os.getenv("LLM_PROVIDER", "ollama").lower()
    model = os.getenv("LLM_MODEL")
    base_url = os.getenv("LLM_BASE_URL")
    api_key = os.getenv("LLM_API_KEY")

    if provider == "ollama":
        if not model or not base_url:
            raise ValueError("LLM_MODEL and LLM_BASE_URL must be set for Ollama")

        return ChatOllama(
            model=model,
            base_url=base_url,
            temperature=0.1,
        )

    elif provider == "openai":
        if not model or not api_key:
            raise ValueError("LLM_MODEL and LLM_API_KEY must be set for OpenAI")

        return ChatOpenAI(
            model=model,
            api_key=api_key,
            base_url=base_url,  
            temperature=0.1,
        )

    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {provider}")


SYSTEM_PROMPT = """
You are a protein structure analysis assistant.

Your role is to help users analyze and assess protein structures in a
scientific and reliable manner.

General rules:
- Only use a tool when it is clearly required to complete the user's request.
- Do NOT guess file paths, parameters, or fabricate results.
- If required information is missing or ambiguous, ask the user for clarification.
- Do NOT run tools speculatively.
- When a tool is used, explain clearly what was done and what the result represents.

Available capability:
- Protein backbone quality assessment and visualization
  (e.g., Ramachandran plot generation).

Respond in a concise, professional, and scientific manner.
"""


def build_agent():
    llm = build_llm()

    tools = [
        plot_ramachandran_tool,
    ]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )

    return agent


def main():
    agent = build_agent()

    print("蛋白质评估助手")
    print("输入你的需求。输入 'exit' 或 'quit' 退出对话.\n")

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
    ]

    while True:
        user_input = input("你: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("天选之蚕: 燕子，下次见面也要幸福！.")
            break

        messages.append(HumanMessage(content=user_input))

        try:
            result = agent.invoke({"messages": messages})
        except Exception as e:
            print(f"出错啦： {e}")
            continue

        messages = result["messages"]
        print(f"天选之蚕: {messages[-1].content}\n")


if __name__ == "__main__":
    main()
