from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self):
        db = self.settings['db']


class User(RequestHandler):
    def get(self, id):
        '''
        Get a single user.
        Requires being authenticated as himself or being admin
        '''
        pass

    def delete(self, id):
        '''
        Deletes a single user.
        Requires being authenticated as himself or being admin
        '''
        pass

class CreateUser(RequestHandler):
    def post(self):
        '''
        Creates a new user.
        '''

class Links(RequestHandler):
    def get(self):
        '''
        Get latest links
        '''
        
