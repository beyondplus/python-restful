import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
from Database import Database

define("port", default=8888, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("template/template.html", title="My title", items=items)

class InsertApiHandler(tornado.web.RequestHandler):
    def post(self):
        body = self.get_argument("body")
        query = """
        INSERT INTO messages
        (`body`)
        VALUES
        ('"""+body+"""')
        """
        db = Database()
        db.insert(query)
        self.write("Retun "+body)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/api/insert", InsertApiHandler)
    ])

def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
    