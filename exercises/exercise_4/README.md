# Exercise 4: Streaming Responses

## Goal

The goal of this exercise is to demonstrate how to stream responses from a language model. This is useful when you want to display the response to the user as it is being generated, rather than waiting for the entire response to be available.

## Steps

1.  **Import necessary libraries**: You will need to import the `connect_to_llm_chat` function from the `config` module.
2.  **Connect to the language model**: Use the `connect_to_llm_chat` function to get a chat model object.
3.  **Create a loop**: Create a `while True` loop to continuously get user input.
4.  **Use the `stream` method**: Inside the loop, call the `stream` method on the chat model object, passing the user's prompt as an argument.
5.  **Print the response**: The `stream` method returns a generator. Iterate over the generator and print the `content` of each part of the response. Use `end=""` and `flush=True` in the `print` function to ensure the response is printed as it is received.

## Solution

```python
from config import connect_to_llm_chat

chat_model = connect_to_llm_chat()

while True:
    prompt = input("User prompt: ")
    # Streaming pattern
    print("\nBot:")
    for part in chat_model.stream(prompt):
        print(part.content, end="", flush=True)
```

