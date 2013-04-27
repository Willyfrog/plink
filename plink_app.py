import tornado
import links
import handlers

db = links.get_mongo_db()
handlers = [
    (r'/', handlers.IndexHandler),
    (r'/u/([0-9]+)', handlers.PreciseUser),
    (r'/u', handlers.User),
    (r'/l/([0-9]+)', handlers.PreciseLink),
    (r'/l', handlers.Link),]

app = tornado.web.Application(handlers, db=db, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.instance().start()
