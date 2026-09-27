from langchain_groq import ChatGroq
from dotenv import load_dotenv
import pandas as pd
import sys
load_dotenv()

llm = ChatGroq(model = "allam-2-7b", temperature=0)

file_path = input("Enter file: ")

if file_path.endswith(".xlsx"):
    df = pd.read_excel(file_path)
    
elif file_path.endswith(".csv"):
    df = pd.read_csv(file_path)

else:
    print("Incorrect file type selected")
    sys.exit()

compact = df.head(20)
stri = compact.to_string()
prompt = [
    {"role":"system", "content":"you are an expert data analyzer and statistics expert"},
    {"role":"user", "content":stri}
]

while True:
    query = input("Enter your query: ")
    if query.lower() == "exit":
        print("bye.....")
        break

    prompt.append(
        {"role":"user", "content":query}
    )

    response = ""
    
    print("\n ai resposne: ", end = "", flush = True)

    for chunk in llm.stream(prompt):
        print(chunk.content, end = "", flush = True)
        response += chunk.content

    prompt.append(
        {"role":"assistant", "content":response}
    )