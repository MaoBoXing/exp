try:
    import requests,os,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    paths = ['/manage','/script']
    tagets = "http://"+ ip +":"+port
    for path in paths:
        try:
            target = tagets+path
            req = requests.get(target,timeout=3,allow_redirects=False)
            if req.status_code == 200:
                logging.info('[+] {} find jenkins unauthorized'.format(ip))
                os._exit(1)
        except Exception as e:
            pass
    
    logging.info("[-] {} do not found jenkins unauthorized".format(ip))
    os._exit(2)

if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)