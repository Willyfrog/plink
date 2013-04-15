import motor
from datetime import datetime

def get_mongo_db(connection_uri=None):
    '''
    stablish a connection with the mongodb
    '''
    client = motor.MotorClient(connection_uri).open_sync()
    db = client.plink_database
    return db

def validate_url(url):
    #FIX-ME: validar que sea una url
    return url

def get_link(db, query={}):
    return Link(db.links.get_one(query))

def get_link_list(db, query={}, limit=None):
    cursor = db.links.find(query)
    if limit is not None:
        cursor.limit(limit)
    return MongoIterator(cursor, Link)

def get_users_links(db, user):
    try:
        user_id = int(user)
    except (TypeError, ValueError):
        user_id = user.get('_id', None)
    if user_id is None:
        return None
        
    return get_link_list(db, {'owner': user_id})

def get_users_list(db, query={}):
    return MongoIterator(db.users.find(query), User)

def get_user(db, query={}):
    return User(db.users.get_one(query))


class MongoIterator:
    '''
    Gets a mongo cursor and returns an Iterator that will transform each document into it's corresponding class
    '''
    def __init__(self, cursor, class_type=None):
        self.cursor = cursor
        self.class_type = class_type

    def next(self):
        if self.cursor.fetch_next() != False:
            if self.class_type != None:
                return self.class_type(self.cursor.next_object())
            else:
                return self.cursor.next_object()
            
        else:
            raise StopIteration
        

class Link:

    def __init__(self, values):
        url = validate_url(values['url'])
        owner = values['owner']
        description = values['description']
        banned = values.get('banned', False)
        _id = values.get('_id', None)

    def _to_dict(self):
        res = {'url': self.url,
               'owner': self.owner,
               'description': self.description,
               'banned': self.banned}
        if self.__id is not None:
            res['_id'] = self._id
            
        return res

    def save(self, db, callback):
        db.links.save(self._to_dict, callback=callback)

    def delete(self, db, callback):
        if self._id is not None:
            db.links.remove({'_id': self._id}, callback=callback)
        else:
            return callback()

class User:

    def __init__(self, values):
        login = values['login']
        password = values['password']
        date_created = values.get('date_created', datetime.now())
        email = values['email']
        disabled = values.get('disabled', False)
        admin = values.get('admin', False)
        _id = values.get('_id', None)

    def _to_dict(self):
        res = {'login': self.login,
               'password': self.password,
               'date_created': self.date_created,
               'admin': self.admin,
               'disabled': self.disabled}
        
        if self.__id is not None:
            res['_id'] = self._id
            
        return res

    def save(self, db, callback):
        db.users.save(self._to_dict, callback=callback)

    def delete(self, db, callback):
        if self._id is not None:
            db.users.remove({'_id': self._id}, callback=callback)
        else:
            return callback()

    def __repr__(self):
        res = self._to_dict()
        res.pop('password')
        return res
