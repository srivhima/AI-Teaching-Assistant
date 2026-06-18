import os
import certifi
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = os.environ.get("DB_NAME", "tutorRag")

if not MONGO_URI:
    raise Exception("MONGO_URI not found")

print("Mongo URI loaded:", MONGO_URI[:25])

client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000
)

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