import os
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "tutorRag")

client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=30000
)

# connection test
client.admin.command("ping")

db = client[DB_NAME]

#user_collection
users_collection = db["users"]
# document collection
chunk_collection = db["text"]
# chat collection
chat_history_collection = db["chat_history"]
# Quiz collection

quizzes_collection = db["quizzes"]
quiz_history = db["history"]

print("MongoDB Connected")