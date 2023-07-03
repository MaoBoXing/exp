#encoding:utf-8
try:
    import requests,os,logging,sys
    requests.packages.urllib3.disable_warnings()
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def main(url):
    
    payload = "                  "                                                      #填写payload
    try:
        req = requests.get(url + payload,timeout=3,verify=False,allow_redirects=False)
        if req.status_code == 200:                                                          #修改匹配返回代码
            if ( "     " in req.text ) and ( "        " in req.text ) and ( '        ' in req.text):          #填写匹配信息
                logging.info(u"[+] {} find     ".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info(u"[-] {} do not found      ".format(ip))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info(u"[-] {} do not found      ".format(ip))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] timeout")
        os._exit(4)

if __name__ == "__main__":
    url = sys.argv[1]
    check(url)
