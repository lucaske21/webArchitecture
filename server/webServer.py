from flask import Flask
from tools import logger
class Webserver:
    def __init__(self, ip: str, port: int, alg: logger.AppLog) -> None:
        self.alg = alg
        self.ipAddress = ip
        self.port = port
        self.app = Flask(__name__)
        self.TAG = "[Webserver]"

    def route(self):
        @self.app.route("/")
        def hello_world():
            logInfo = [self.TAG, "Route", "hello_world", "invoked"]
            self.alg.critical(logInfo)
            return "<p>Hello, World!</p>"
    
    def run(self):
        self.route()
        self.app.debug = False
        self.app.templates_auto_reload = False
        self.app.run(host=self.ipAddress, port=self.port)