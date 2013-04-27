from tornado.web import RequestHandler, HTTPError
from model import links, user
class PreciseUser(RequestHandler):
    def get(self, id):
        '''
        Get a single user.
        Requires being authenticated as himself or being admin
        '''
        res = links.get_user({'id':id})
        if res is not None:
            self.set_status(200)
            self.write(res)
        raise HTTPError(404, "User not found")

    def put(self, id):
        '''
        Replace info for a user
        '''
        res = links.get_user({'id':id})
        if res is not None:
            #FIXME: modify
            self.set_status(200)
            self.write(res)
        raise HTTPError(404, "User not found")
    
    def delete(self, id):
        '''
        Deletes a single user.
        Requires being authenticated as himself or being admin
        '''
        res = links.get_user({'id':id})
        if res is not None:
            #FIXME: delete
            self.set_status(204)
            self.write("")
        raise HTTPError(404, "User not found")

class User(RequestHandler):
    def post(self):
        '''
        Creates a new user.
        '''
        params = self.request.arguments.copy()
        #FIXME: validate parameters
        #FIXME: autenticar mediante sesion o token
        new_user = User(params)
        self.set_status(201)
        self.write(new_user)

    def get(self):
        '''
        Gets a list of users.
        '''
        db = self.settings['db']
        users = user.get_users_list(db)
        self.set_status(200)
        self.write("[")
        first = True
        for u in users:
            if not first:
                self.write(',')
            else:
                first = False
                
            self.write(u)

        self.write("]")
