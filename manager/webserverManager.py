from server import webServer
from tools import logger
import threading


def manager(alg: logger.AppLog, ip: str, port: int):
    webserver = webServer.Webserver(ip, port, alg=alg)
    webserver.run()
    

    
