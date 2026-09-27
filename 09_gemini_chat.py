from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-3.7-flash", temperature=0)

prompt = [
    {"role":"system", "content":"you are a friendly system yet smart"},

]

while True:
    query = input("Enter the query: ")
    if query.lower() == "exit":
        print("Google model says bye!")
        break

    prompt.append(
        {"role":"user", "content":query}
    )

    response = ""

    print("\nai response\n", end = "", flush = True)
    for chunk in llm.stream(prompt):
        print(chunk.text, end = "", flush = True)
        response += chunk.text

    prompt.append(
        {"role": "assistant", "content":response}
    )