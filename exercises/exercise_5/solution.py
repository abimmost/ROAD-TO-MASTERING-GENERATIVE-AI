from configs  import load_google_chat_model

chat = load_google_chat_model

print("THE AI ASSISTANT WELCOMES YOU")
print("-"*30,"\n Begin by entering a prompt")

while True:
    prompt = input("USER: ")
    if prompt.lower() == "quit" or "exit":
        print("Goodbyte...")
        break
    for part in chat.stream(prompt):
        print(part, end="", flush=True)