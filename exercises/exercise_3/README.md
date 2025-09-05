# Exercise 3: Basic Chat Model Interaction

**Objective**: Build conversational interactions using chat models

**Concepts**: Chat models, Message formatting, System prompts, Conversation flow

### Instructions

1. Load a Google chat model from your config
2. Create a message structure with system and user roles
3. Use the chat model to respond to questions
4. Experiment with different system prompts to change AI behavior

### Starter Code

```python
from config import load_google_chat_model

# TODO: Load chat model
# TODO: Create messages array with system and user messages
# TODO: Get response using invoke()
# TODO: Test different system prompts
```

### Expected Message Format
```python
messages = [
    ("system", "You are a helpful assistant specialized in..."),
    ("user", "Your question here")
]
```

### Challenge
Create different personas by changing the system message and test how responses change.
