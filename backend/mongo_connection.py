# mongo_connection.py
from pymongo import MongoClient

# Replace with your actual connection string
MONGO_CONNECTION_STRING = "mongodb://localhost:27017/edubooking"  # or your MongoDB Atlas connection string

# Create a client
client = MongoClient(MONGO_CONNECTION_STRING)

# Access the database
db = client['edubooking']  # Replace with your actual database name
