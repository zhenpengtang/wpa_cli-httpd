import tornado.ioloop
import tornado.web
import yaml

f=open("config.yaml")
config=yaml.load(f)



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates\index.html",smslist=[])
class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates\test.html")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/test.html", TestHandler),
        (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": config["js"]}),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": config["css"]}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()