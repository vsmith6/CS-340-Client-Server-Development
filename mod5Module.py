from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        
        self.client = MongoClient('mongodb://%s:%s@localhost:38598/AAC' % (username,
                                                                           password))
        self.database = self.client['AAC']

        
       

# create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)
            print(insert)
            if insert!=0:
                return True
            else:
                return False           
        else:
            raise Exception("Nothing to save, because data parameter is empty")


# create method to implement the R in CRUD.
    def read(self,criteria=None):

        # criteria is present it will find the item by -id
        if criteria:
            data = list(self.database.animals.find(criteria,{"_id":False}))
            return data

        else:
        #if there is nothing to find, the search will be false
            data = self.database.animals.find( {} , {"_id":False})
            raise Exception("Data is empty")
            return False
        
# cursor method to return all results from the animals collection
    def read_all(self,data): 
        cursor = self.database.animals.find(data,
                                            {'_id':False} )
        return cursor
        
# update method in crud - update method takes self, the data to be changed, and the new data as parameters
    def update(self, old_data,
               new_data):
        #proceed is there is old data
        if old_data is not None:
            #log success message to the console
            print("Successfully Updated")
            # using the self as the instance of the database and update_many to change the old_data to the new_data passed in
            return self.database.animals.update_many(old_data, {'$set':new_data}) #updating the animal data in the collection
        else:
            #raise and exception is there is no data to update
            raise Exception("Nothing to Update, data parameters are empty")
            return False
        
# delete method in crud - delete method takes self and the data to be deleted as parameters
    def delete(self, data):
        if data is not None:
            try:
                # use the delete_one method with self as the database instance to delete the data passed into the function
                delete_result = self.database.animals.delete_one(data)
                # print the success message to the console
                print("Successfully Deleted")
                return True
            # if an error occurs, throw an exception
            except Exception as e:
                print("Exception occured: ", e)
        else:
            # if there is no data passed in, raise an exception to alert the user
            raise Exception("Nothing to delete, data is empty")
            return False  
 
    
        
    

    
        