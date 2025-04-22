# animalShelter.py
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        # USER = 'aacuser'
        # PASS = 'Test1234!'
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33043
        DB = 'AAC'
        COL = 'animals'

        try:
            # Initialize MongoDB connection
            self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
            self.database = self.client[DB]
            self.collection = self.database[COL]
            print("===Connection to MongoDB successful!")
        except Exception as e:
            print(f"===Error connecting to MongoDB: {e}")
            raise

    def create(self, data):
        """Insert a new document into the collection."""
        if data:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except Exception as e:
                print(f"===Error inserting document: {e}")
                return False
        else:
            raise Exception("===Nothing to save, because data parameter is empty")

    def read(self, query):
        """Read documents from the collection based on a query."""
        try:
            documents = list(self.collection.find(query))
            return documents
        except Exception as e:
            print(f"===Error reading documents: {e}")
            return []
    
    def update(self, query, newDocs):
        """Update documents in the collection based on a query."""
        if query and newDocs:
            try:
                result = self.collection.update_many(query, {"$set": newDocs})
                return result.modified_count
            except Exception as e:
                print(f"===Error updating document(s): {e}")
                return []
        else:
            raise Exception("===Missing query or update values")

    def delete(self, query):
        """Delete documents from the collection based on a query."""
        if query:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"===Error deleting document(s): {e}")
                return []
        else:
            raise Exception("===Missing query for delete operation")

