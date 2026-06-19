import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "tutorRag")

print("Mongo URI loaded:", MONGO_URI[:25])

client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=30000
)


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