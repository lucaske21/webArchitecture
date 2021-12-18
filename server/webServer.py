from flask import Flask

class Webserver:
    def __init__(self, ip, port) -> None:
        self.ipAddress = ip
        self.port = port
        self.app = Flask(__name__)

    def route(self):
        @self.app.route("/")
        def hello_world():
            return "<p>Hello, World!</p>"
    
    def run(self):
        self.route()
        self.app.debug = False
        self.app.templates_auto_reload = False
        self.app.run(host=self.ipAddress, port=self.port)