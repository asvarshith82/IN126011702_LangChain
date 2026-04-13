from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

def main():
    template = PromptTemplate(
        input_variables=["topic"],
        template="Explain the concept of {topic} in simple terms."
    )

    prompt = template.format(topic="LangChain")

    llm = ChatOpenAI(model="gpt-4o-mini")

    response = llm.invoke(prompt)
    print(response.content)


if __name__ == "__main__":
    main()