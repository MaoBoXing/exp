import sys,os,logging,requests
logging.basicConfig(level=logging.INFO,format="%(message)s")
def check(ip,port):
    trget = "http://"+ip + ":" + port + "/actuator/env"

    req = requests.get(trget,timeout=3)

    if req.status_code == 200:
        if b"PID" in req.text:
            logging.info("[+] {} find spring boot unauthorized".format(ip))
            os._exit(1)
        else:
            logging.info("[-] {} do not found spring unauthorized".format(ip))
            os._exit(2)
    else:
        logging.info("[-] {} do not found spring unauthorized".format(ip))
        os._exit(2)


if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)