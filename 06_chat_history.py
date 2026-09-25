from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model = "allam-2-7b")

prompt = [
    (
        "system",
        "You are a friendly assistant. "
        "Always respond in English only. "
        "Never respond in Arabic or any other language, "
        "even if the user uses another language."
    )
]

while True:
    query = input("\nenter your query: ")

    if query.lower() == "exit":
        print("exit is done!")
        break

    prompt.append(
        ("user", query)
    )

    response = ""

    print("\n ai response\n: ", end = "", flush = True)
    for chunk in llm.stream(prompt):
        print(chunk.content, end = "", flush = True)
        response += chunk.content

    prompt.append(
        ("assistant", response)
    )