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
        users = get_users_list(self.db)
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

class Link(RequestHandler):
    def get(self):
        '''
        Get latest links
        '''
        links = get_links_list(self.db, limit=10)
        self.set_status(200)
        self.write("[")
        first = True
        for l in links:
            if not first:
                self.write(',')
            else:
                first = False
                
            self.write(l)

        self.write("]")

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
