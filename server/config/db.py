import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

print("DB_NAME =", DB_NAME)
print("URI loaded =", bool(MONGO_URI))

client = MongoClient(
    os.getenv("MONGO_URI"),
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=30000,
    connect=False
)

db = client.get_database(DB_NAME)

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