from tornado.web import RequestHandler, HTTPError

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
