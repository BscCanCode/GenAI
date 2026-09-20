from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Initialize your environment keys securely
load_dotenv()

# THE FIX: Targeting the primary model ID visible in your Limits panel
llm = ChatGroq(model="allam-2-7b")

prompts = [
    ("system", "you are a 10 year old kid"),
    ("user", "how to sort python list")
]
# Explicitly request English in your string prompt to stop any language shifting
res = llm.stream(prompts)

# CRITICAL: Use .content to strip away the messy metadata block
print(res)
