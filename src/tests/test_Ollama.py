from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

def main():
    llm = Ollama(
        model="modelscope.cn/Qwen/Qwen3-4B-GGUF:latest",
        base_url="http://localhost:11434",
        temperature=0.1,
    )

    prompt = PromptTemplate.from_template(
        "你是ollama，请用{n}句话回答：{q}"
    )

    chain = prompt | llm

    resp = chain.invoke({"n": 1, "q": "你好ollama"})
    print(resp)

if __name__ == "__main__":
    main()
