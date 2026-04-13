from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI

def main():
    llm = ChatOpenAI(model="gpt-4o-mini")

    memory = ConversationBufferMemory()

    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )

    print(conversation.predict(input="Hello"))
    print(conversation.predict(input="What did I just say?"))


if __name__ == "__main__":
    main()