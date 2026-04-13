from langchain.agents import initialize_agent, Tool
from langchain.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI

def main():
    search = DuckDuckGoSearchRun()

    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="Useful for searching the internet"
        )
    ]

    llm = ChatOpenAI(model="gpt-4o-mini")

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )

    result = agent.run("Latest developments in generative AI")
    print(result)


if __name__ == "__main__":
    main()