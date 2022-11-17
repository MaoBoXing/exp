#encoding:utf-8


try:
    import os
    import requests
    import logging
except:
    os._exit(6)
    
logging.basicConfig(level=logging.INFO,format='%(message)s')
def check(ip,port):
    url = "http://"+ip + ':' + str(port)+"/cluster"
    try:
        get = requests.get(url,timeout=1)
    except:
        logging.info("[*] time out")
        return 4
    try:
        if get.status_code== 200:
            logging.info("[+] {} find hadoop unauthorized".format(ip))
            return 1
        logging.info("[-] {} do not found hadoop unauthorized".format(ip))
        return 2
    except Exception as e:
        logging.info("[*] something error!!")
        return 3

def main(ip,port):
    get =  check(ip,port)
    os._exit(get)

if __name__ == '__main__':
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))