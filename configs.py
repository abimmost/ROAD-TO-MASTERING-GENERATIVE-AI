# config.py
import os
from config import connect_to_llm, connect_to_llm_chat, connect_to_groq

def load_google_llm():
    llm = connect_to_llm()
    return llm

def load_google_chat_model():
    chat_model = connect_to_llm_chat()
    return chat_model

def load_groq_chat_model():
    groq_model = connect_to_groq()
    return groq_model

def select_model():
    print("\nAvailable Models:")
    print("1. Google LLM")
    print("2. Google Chat Model")
    print("3. Groq Chat Model")
    
    while True:
        try:
            choice = int(input("\nSelect a model (1-3): "))
            if choice == 1:
                return load_google_llm()
            elif choice == 2:
                return load_google_chat_model()
            elif choice == 3:
                return load_groq_chat_model()
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

