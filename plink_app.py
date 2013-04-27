import tornado
from model.plink_motor import get_mongo_db
from routes import handlers

db = get_mongo_db()

app = tornado.web.Application(handlers, db=db, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.instance().start()
