from pymongo import MongoClient

DB_USERNAME = "interviewee"
DB_PASSWORD = "<ask-interviewer>"
URI = f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@cluster0.dzwwge0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a reusable MongoClient object
client = MongoClient(URI, serverSelectionTimeoutMS=5000)


def start():
    try:
        db = client.get_database("sports")
        print("Database connection opened!")
    except Exception as e:
        print("Unable to connect to MongoDB:", e)
