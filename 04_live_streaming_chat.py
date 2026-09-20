from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model = "allam-2-7b")
my_question = input("Enter your query: ")

prompt = [
    ("system","act as a brilliant ai"),
    ("user", my_question)
]
print("\nai response", end = "", flush=True)
res = llm.stream(prompt)
for chunks in res:
    print(chunks.content, end="", flush=True)