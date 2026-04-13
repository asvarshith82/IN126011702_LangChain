from langchain_openai import ChatOpenAI

def main():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7
    )

    response = llm.invoke("Explain LangChain in simple terms.")
    print(response.content)


if __name__ == "__main__":
    main()