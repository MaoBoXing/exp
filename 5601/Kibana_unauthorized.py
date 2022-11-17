try:
    import os,logging,requests
    logging.basicConfig(level=logging.INFO ,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    try:
        target = "http://" + ip +":"+port+"/app/kibana#"
        req = requests.get(target,timeout=3)
        if b'Dev Tools' in req.text:
            logging.info("[+] {} find kibana unauthorized".format(ip))
            os._exit(1)
        else :
            logging.info('[-] {} do not found kibana unauthorized'.format(ip))
            os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__ =="__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
