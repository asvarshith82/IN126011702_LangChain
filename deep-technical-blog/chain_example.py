from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

def main():
    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = PromptTemplate(
        input_variables=["topic"],
        template="Write a short explanation about {topic}"
    )

    chain = LLMChain(
        llm=llm,
        prompt=prompt
    )

    result = chain.run("LangChain architecture")
    print(result)


if __name__ == "__main__":
    main()