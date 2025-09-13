from configs import load_google_chat_model

chat_model = load_google_chat_model()

while True:
    prompt = input("User prompt: ")
    # Streaming pattern
    print("\nBot:")
    for part in chat_model.stream(prompt):
        print(part.content, end="", flush=True)