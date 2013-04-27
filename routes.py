from handler import plink, user_handler, link_handler

handlers = [
    (r'/', plink.IndexHandler),
    (r'/u/([0-9]+)', user_handler.PreciseUser),
    (r'/u', user_handler.User),
    (r'/l/([0-9]+)', link_handler.PreciseLink),
    (r'/l', link_handler.Link),]
