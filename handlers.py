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
        users = links.get_users_list(db)
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
        db = self.settings['db']
        link_list = links.get_link_list(db, limit=10)
        self.set_status(200)
        self.write("[")
        first = True
        for l in link_list:
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
        values = {
            'url': self.get_argument('url'),
            'owner': 1, #TODO: usar sesion
            'description': self.get_argument('description', ''),
            'banned': False}
        
            

class PreciseLink(RequestHandler):
    def get(self, id):
        '''
        get info from a link
        '''
        #FIXME: cerrar a solo publicos o propios
        link = links.get_link({'id':id})
        if link is not None:
            raise HTTPError(404, "Link not found")
        self.set_status(200)
        self.write(link)

class Authenticate(RequestHandler):
    def post(self):
        '''
        validate user
        '''
        pass
