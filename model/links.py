from datetime import datetime
from utils import parse_iso_datetime
from plink_motor import MongoIterator

def validate_url(url):
    #FIX-ME: validar que sea una url
    return url

def get_user_link(db, user, query={}):
    return Link(db[user].get_one(query))

def get_user_link_list(db, user, query={}, limit=None):
    cursor = db[user].find(query)
    if limit is not None:
        cursor.limit(limit)
    return MongoIterator(cursor, Link)

def get_all_links(db, user):
    #FIXME
    #NotSureIfNecessary
    pass    

class Link (object):
    """
    converts from link document to python object
    """
        
    def __init__(self, values):
        self.url = validate_url(values['url'])
        self.owner = values['owner']
        self.description = values['description']
        self.banned = values.get('banned', False)
        self._id = values.get('_id', None)
        self.tags = values.get('tags', None)
        self.date_added = parse_iso_datetime(datetime.values.get('date_added', None)) or datetime.utcnow()

    def _to_dict(self):
        res = {'url': self.url,
               'owner': self.owner,
               'description': self.description,
               'banned': self.banned}
        if self._id is not None:
            res['_id'] = self._id
            
        return res

    def save(self, collection, callback):
        """
        saves document to a collection
        """
        
        collection.save(self._to_dict, callback=callback)

    def delete(self, collection, callback):
        """
        removes a document from a collection
        """
        
        if self._id is not None:
            collection.remove({'_id': self._id}, callback=callback)
        else:
            return callback()

