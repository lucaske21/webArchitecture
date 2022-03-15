from manager import webserverManager
from tools import logger
import threading
import sys
import time

def main():
    alg = logger.AppLog()
    appRunningEvent = threading.Event()
    ip = "127.0.0.1"
    port = 5001
    tWebserver = threading.Thread(target=webserverManager.manager, args=(alg, ip, port))
    tWebserver.setDaemon(True)
    tWebserver.setName("webserver")
    tWebserver.start()
    
    while True:
        try:
            time.sleep(2)
            if appRunningEvent.is_set():
                pass
        except KeyboardInterrupt:
            
            # alg.critical("All thread has been stop")
            alg.critical("By KeyboardInterrupt")
            sys.exit()



if __name__ == '__main__':
    main()