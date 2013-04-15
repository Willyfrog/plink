import tornado
import links
import handlers

db = links.get_mongo_db()
handlers = [(r'/', handlers.IndexHandler)]

app = tornado.web.Application(handlers, db=db)
app.listen(8888)
tornado.ioloop.IOLoop.instance().start()
