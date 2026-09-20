from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model = 'allam-2-7b')
my_question = input("Enter your question: ")

prompt = [
    ('system', 'act as a java developer'),
    ('user', my_question)
]
res = llm.invoke(prompt)
print(res.content)