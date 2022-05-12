#encoding:utf-8
#anthor:Pocosin
try:
    import os
    import logging
    import requests
except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')
def check(ip, port):
    try:
        url = "http://"+ip+":"+str(port)+"/_cat"
        response = requests.get(url,timeout=2) 
    except:
        logging.info("[*] {} time out".format(ip))
        return 4
    try:
        if "/_cat/master" in response.content:
            logging.info("[+] {} find elasticsearch unauthorized".format(ip))
            return 1
        logging.info("[-] do not found elasticsearch unauthorized".format(ip))
        return 2
    except:
        logging.info("[*] Something Error!!")
        return 3
def main(ip,port):
    get =  check(ip,port)
    os._exit(get)

if __name__ == '__main__':
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,port)
    