# ================================
# Importing necessary libraries
# ================================
from bot import ask_bot
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

# ======================================
# FASTAPI PART
# ======================================

app = FastAPI(title="Mini-Health ChatBot API")

# OPTIONAL: CORS for frontend usage
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # <-- allow all domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Request body model
class ChatRequest(BaseModel):
    question: str = Field(examples=["What is the best way to maintain an healthy life in a few words?"])


# Endpoint
@app.get("/")
def get_root():
    return "Welcome to my mini-health Chatbot"

@app.post("/ask")
def ask_chatbot(chat: ChatRequest):
    answer = ask_bot(chat.question)
    return {"answer": answer}
