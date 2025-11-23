# Importing necessary libraries
from openai import OpenAI
from dotenv import load_dotenv
from yaspin import yaspin
import os

# Loading the .env file
load_dotenv()

# Fetch the key form the dotenv to a variable name
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError ("API key not found!")

client = OpenAI(api_key=api_key)

# ======================================
# CHATBOT CONFIGURATION & PERSONA
# ======================================
SYSTEM_PROMPT = (
    "You are a strictly health-focused AI assistant. "
    "You must only answer questions related to health, fitness, nutrition,"
    "diseases, medications, medical advice, anatomy, physiology, or wellbeing. "
    "If the user asks anything outside health, politely decline. "
    "Never provide instructions that could cause harm. "
    "If a question requires urgent medical attention, instruct the user to see a doctor immediately. "
    "Format all responses as clean plain text with no markdown or special characters."
)
# ================================
        # Model configuration
# ================================
MODEL_NAME = "gpt-5-chat-latest"
TEMPERATURE = 0.2
TOP_P = 0.9
MAX_OUTPUT_TOKENS = 400

# Limit chat history size
MAX_HISTORY = 10  # last 10 messages only


# Maintain a list for chat history
chat_history = []


# ======================================
        # Function to Ask the Bot
# ======================================
def ask_bot(user_message: str) -> str:
    """
    Sends a question to the health bot and returns the response.
    Keeps context history so the bot can remember previous messages.
    """
        
    # Add user message to history
    chat_history.append({"role": "user", "content": user_message})
    
    # Build input with system prompt & history
    input_messages = [
        {"role": "system", "content": SYSTEM_PROMPT}] + chat_history
    
    # Nice loading state (terminal mode)
    with yaspin(text="Bot thinking...", color="cyan"):
        response = client.responses.create(
        model=MODEL_NAME,
        input=input_messages,
        temperature=TEMPERATURE,
        top_p=TOP_P,
        max_output_tokens=MAX_OUTPUT_TOKENS
        )
        
    answer = response.output_text.strip()
        
    # Update bot's answer to history
    chat_history.append({"role": "assistant", "content": answer})
    
    # Validate chat history
    if len(chat_history) > MAX_HISTORY:
        chat_history[:] = chat_history[-MAX_HISTORY:]

    return answer



# Optional code for running continuous on Terminal
if __name__ == "__main__":
    print("Mini-Health ChatBot (type 'exit' to quit)")
    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        answer = ask_bot(user_input)
        print(f"\nBot: {answer}")
