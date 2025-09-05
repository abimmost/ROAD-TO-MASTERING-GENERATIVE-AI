# Exercise 2: Your First LLM Completion

**Objective**: Use a completion model to generate text responses

**Concepts**: LLM completion, Basic prompting, Streaming responses

### Instructions

1. Load a Google completion model using your config
2. Create a simple prompt about a topic you're interested in
3. Get a response using the `invoke()` method
4. Implement streaming to see the response generated in real-time

### Starter Code

```python
from config import load_google_llm

# TODO: Load the model
# TODO: Create a prompt
# TODO: Get response using invoke()
# TODO: Implement streaming with stream()
```

### Expected Behavior
- See immediate response with invoke()
- Watch text appear word-by-word with streaming
- Handle the response content properly

### Challenge
Create a simple loop that accepts user prompts and responds using the completion model.
