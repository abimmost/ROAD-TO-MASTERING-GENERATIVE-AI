from config import connect_to_llm
import time

llm = connect_to_llm()
prompt = "Why do trees go barren?"

response = llm.invoke(prompt)
print("Response from invoke:\n", response)

time.sleep(4)

print("\n\nResponse from stream:")
for part in llm.stream(prompt):
    print(part, end="", flush=True)