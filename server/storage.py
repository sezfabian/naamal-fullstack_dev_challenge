#!/usr/bin/env python3
from pymongo import MongoClient
required_keys = ["name", "email", "subject", "message"]

class DBStorage:
    """
    This contains the MongoDB storage class
    """

    __engine = None
    __session = None
    mongo_collection = None

    def __init__(self, mongo_collection: str = 'submissions'):
        """
        Initializes the DBStorage class
        """
        self.__engine = MongoClient('mongodb://localhost:27017')
        self.__session = self.__engine['form_submissions']
        self.mongo_collection = mongo_collection

    def get_all_submissions(self):
        """
        Retrieves a list of all stored submissions
        """
        collection = self.__session[self.mongo_collection]
        submissions = list(collection.find({}))
        
        return submissions
    
    def insert_submission(self, submission):
        """
        Inserts a new submission into the database
        """
        if all(key in submission and submission[key] is not None for key in required_keys):
            collection = self.__session[self.mongo_collection]
            collection.insert_one(submission)
        else:
            raise ValueError("Failed to insert submission: Missing one or more required keys.")

    def delete_submission(self, submission):
        """
        Deletes a submission from the database
        """
        collection = self.__session[self.mongo_collection]
        collection.delete_one(submission)
