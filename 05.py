from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(model = "allam-2-7b")

while True:
    my_question = input("\nEnter your query: ")

    if my_question.lower() == "exit":
        print("Exit is done!")
        break

    prompt = [
        ("system", "act as an excellent system"),
        ("user", my_question)
    ]

    print("\nAi response\n", end = "", flush=True)

    for chunks in llm.stream(prompt):
        print(chunks.content, end="", flush=True)