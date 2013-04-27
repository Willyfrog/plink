from tornado.web import RequestHandler, HTTPError
import links

class IndexHandler(RequestHandler):
    def get(self):
        db = self.settings['db']


class Authenticate(RequestHandler):
    def post(self):
        '''
        validate user
        '''
        pass
