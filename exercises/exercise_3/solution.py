from config import connect_to_llm_chat

llm_chat = connect_to_llm_chat()
messages = [
    ("system", "You are a helpful assistant specialized in human anatomy"),
    ("user", "Can digestive acid in my stomach be secreted even without food in it?")
]
response = llm_chat.invoke(messages)
print(f"Assistant: {response}")