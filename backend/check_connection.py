from pymongo import MongoClient, errors

def check_connection():
    try:
        # Replace 'localhost' and '27017' with your MongoDB host and port if different
        client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=5000)
        
        # Attempt to retrieve server information
        client.server_info()  # This will raise an exception if the connection fails
        
        print("You are connected to the database!")
    except errors.ServerSelectionTimeoutError as err:
        print("Connection failed: ", err)

if __name__ == "__main__":
    check_connection()
