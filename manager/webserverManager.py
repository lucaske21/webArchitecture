from server import webServer
import threading


def manager():
    ip = "127.0.0.1"
    port = 5001
    webserver = webServer.Webserver(ip, port)
    webserver.run()
    

    
