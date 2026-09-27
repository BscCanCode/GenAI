from langchain_groq import ChatGroq
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv('iris.csv')
print(df)

df1 = df.head(10).to_string()

llm = ChatGroq(model = "allam-2-7b", temperature=0)

prompt = [
    {"role":"system", "content":"you are an csv file reader and statistics expert"},
    {"role":"user", "content": df1}
]

while True:
    query = input("enter the query: ")
    if query.lower()=="exit":
        print("bye....")
        break

    prompt.append(
        {"role":"user", "content": query}
    )

    print("\nai response\n", end = "", flush = True)
    response = ""
    for chunk in llm.stream(prompt):
        print(chunk.content, end = "", flush = True)
        response += chunk.content

    prompt.append(
        {"role":"assistant", "content": response}
    )