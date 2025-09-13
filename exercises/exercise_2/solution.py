from configs import load_google_llm
import time

llm = load_google_llm()
while True:
    prompt = input("\nEnter your prompt: ")

    # response = llm.invoke(prompt)
    # print("Response from invoke:\n", response)

    # time.sleep(4)

    print("\nResponse from stream:")
    for part in llm.stream(prompt):
        print(part, end="", flush=True)