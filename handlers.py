from tornado.web import RequestHandler, HTTPError
import links

class IndexHandler(RequestHandler):
    def get(self):
        db = self.settings['db']


class PreciseUser(RequestHandler):
    def get(self, id):
        '''
        Get a single user.
        Requires being authenticated as himself or being admin
        '''
        res = links.get_user({'id':id})
        if res is not None:
            self.write(200, res)
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
        new_user = User(params)
        self.set_status(201)
        self.write(new_user)

    def get(self):
        '''
        Gets a list of users.
        '''
        

class Link(RequestHandler):
    def get(self):
        '''
        Get latest links
        '''
        pass

    def post(self):
        '''
        Add a new link
        '''
        pass

class PreciseLink(RequestHandler):
    def get(self, id):
        '''
        get info from a link
        '''
        pass
