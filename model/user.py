from datetime import datetime
from utils import parse_iso_datetime
from plink_motor import MongoIterator

def get_users_list(db, query={}):
    return MongoIterator(db.users.find(query), User)

def get_user(db, query={}):
    return User(db.users.get_one(query))


class User:
    """
    converts from user document to python object
    """
    
    def __init__(self, values):
        self.login = values['login']
        self.password = values['password']
        self.date_created = parse_iso_datetime(values.get('date_created', None)) or datetime.utcnow()
        self.email = values['email']
        self.disabled = values.get('disabled', False)
        self.admin = values.get('admin', False)
        self._id = values.get('_id', None)

    def _to_dict(self):
        res = {'login': self.login,
               'password': self.password,
               'date_created': self.date_created,
               'admin': self.admin,
               'disabled': self.disabled}
        
        if self._id is not None:
            res['_id'] = self._id
            
        return res

    def save(self, db, callback):
        db._users.save(self._to_dict, callback=callback)

    def delete(self, db, callback):
        if self._id is not None:
            db._users.remove({'_id': self._id}, callback=callback)
        else:
            return callback()

    def __repr__(self):
        res = self._to_dict()
        res.pop('password')
        return res
