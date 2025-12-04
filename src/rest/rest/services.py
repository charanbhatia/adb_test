from pymongo import MongoClient
from bson import ObjectId
import os

class TodoService:
    def __init__(self):
        mongo_uri = 'mongodb://' + os.environ.get("MONGO_HOST", "localhost") + ':' + os.environ.get("MONGO_PORT", "27017")
        self.db = MongoClient(mongo_uri)['test_db']
        self.collection = self.db['todos']

    def get_all_todos(self):
        todos = []
        for todo in self.collection.find():
            todo['_id'] = str(todo['_id'])
            todos.append(todo)
        return todos

    def create_todo(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)
