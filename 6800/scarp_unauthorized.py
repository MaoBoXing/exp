try:
    import os,requests,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {} ".format(e))
    os._exit(6)

def check(ip,port):
    try:
        target = "http://" + ip + ":" + port +"/addversion.json"
        req = requests.get(target,timeout=3)
        if req.status_code == 200:
            logging.info("[+] {} find scarp unauthorized".format(ip))
            os._exit(1)
        else:
            logging.info("[-] {} do not found scarp unauthorized".format(ip))
            os._exit(2)
    except Exception as e:
        logging.info("[*] {}" .format(ip))
        os._exit(4)

if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)