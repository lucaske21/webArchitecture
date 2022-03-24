from server import webServer
from tools import logger
import threading
import time

class WebManager:
    def __init__(self, alg: logger.AppLog, ip: str, port: int) -> None:
        self.tag = "[WebManager]"
        self.alg = alg
        self.ip = ip
        self.port = port
        self.webserverThread = None
        
    
    def manager(self):
        webserver = webServer.Webserver(self.ip, self.port, alg=self.alg)
        webserver.run()


    def start(self):
        try:
            if self.webserverThread is None:
                self.webserverThread = threading.Thread(target=self.manager, args=())
                self.webserverThread.setDaemon(True)
                self.webserverThread.setName("webserver")
                self.webserverThread.start()
            else:
                self.alg.error([self.tag, "webserverThread has been created!"])
        except Exception as e:
            self.alg.critical([self.tag, e])

    def stop(self):
        try:
            while self.webserverThread.is_alive():
                self.webserverThread.terminate()
                time.sleep(1)
            self.alg.warning([self.tag, "webserverThread has been stopped"])
            
        except Exception as e:


            self.alg.exception([self.tag, e])
    
