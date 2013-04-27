import motor
import pymongo
import sys


def get_mongo_db(connection_uri=None):
    '''
    stablish a connection with the mongodb
    '''
    try:
        client = motor.MotorClient(connection_uri).open_sync()
    except pymongo.errors.ConnectionFailure:
        
        if connection_uri is None:
            print "Mongo is wasn't found on the default place, check if mongodb is running and if the application is properly configured"
        else:
            print "mongo wasn't found running in: %s" % connection_uri
            
        sys.exit(-1)  # Exit to shell
        
    db = client.plink_database
    return db

class MongoIterator:
    '''
    Gets a mongo cursor and returns an Iterator that will transform each document into it's corresponding class
    '''
    def __init__(self, cursor, class_type=None):
        self.cursor = cursor
        self.class_type = class_type

    def __iter__(self):
        return self
        
    def next(self):
        new_doc = self.cursor.next_object()
        if new_doc is not None:
            print "new_doc %s" % new_doc
            if self.class_type != None:
                return self.class_type(new_doc)
            else:
                return self.cursor.next_object()
            
        else:
            raise StopIteration
