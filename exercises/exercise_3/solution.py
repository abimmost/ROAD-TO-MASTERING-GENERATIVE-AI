from configs import load_google_chat_model

llm_chat = load_google_chat_model()
messages = [
    ("system", "You are a helpful assistant specialized in human anatomy"),
    ("user", "Can digestive acid in my stomach be secreted even without food in it?")
]
response = llm_chat.invoke(messages)
print(f"Assistant: {response}")