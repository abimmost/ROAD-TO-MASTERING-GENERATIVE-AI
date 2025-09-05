def environment_settings():
    import os
    from dotenv import load_dotenv, find_dotenv
    
    try:
        # Load environment variables
        if not load_dotenv(find_dotenv()):
            raise EnvironmentError("No .env file found")
        
        # Get API keys
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        
        # Validate API keys
        missing_keys = []
        if not GOOGLE_API_KEY:
            missing_keys.append("GOOGLE_API_KEY")
        if not GROQ_API_KEY:
            missing_keys.append("GROQ_API_KEY")
        
        if missing_keys:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_keys)}")
        
        return True
        
    except ValueError as ve:
        print(f"Environment Error: {ve}")
        print("Please check your .env file and ensure all required API keys are set.")
        return False
    except EnvironmentError as ee:
        print(f"Environment Error: {ee}")
        print("Please make sure .env file exists in the project root directory.")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def connect_to_llm():
    from langchain_google_genai import GoogleGenerativeAI
    llm=GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    return llm
def connect_to_llm_chat():
    from langchain_google_genai import ChatGoogleGenerativeAI
    llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    return llm
def connect_to_groq():
    from langchain_groq import ChatGroq
    llm=ChatGroq(model="deepseek-r1-distill-llama-70b", temperature=0.7)
    return llm

def connect_to_db_url():
    import os
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    DATABASE_URL = os.getenv("DATABASE_URL")
    print(f"Database URL: {DATABASE_URL}")
    return DATABASE_URL

def select_model():
    print("\nAvailable Models:")
    print("1. Google LLM")
    print("2. Google Chat Model")
    print("3. Groq Chat Model")
    
    while True:
        try:
            choice = int(input("\nSelect a model (1-3): "))
            if choice == 1:
                return connect_to_llm()
            elif choice == 2:
                return connect_to_llm_chat()
            elif choice == 3:
                return connect_to_groq()
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")