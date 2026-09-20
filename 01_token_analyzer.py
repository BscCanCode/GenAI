import tiktoken
text = "who are you?"
token = tiktoken.encoding_for_model(model_name="gpt-4")

toks = token.encode(text)
print(toks)

for i in toks:
    chunk = token.decode([i])
    print(f"{i} chunk: {chunk}")

result = [14965, 527, 499, 30]
dec = token.decode(result)
print(dec)