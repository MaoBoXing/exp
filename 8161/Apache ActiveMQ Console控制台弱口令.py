#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    header =  {
                "Authorization": "Basic YWRtaW46YWRtaW4="
                        }
    payload = "/admin"                                                      #填写payload
    try:
        tar = "http://" + ip + ":" + port + payload
        req = requests.get(tar,headers=header,timeout=3)
        if req.status_code == 200:                                                          #修改匹配返回代码
            if  b"Version" in req.text :          #填写匹配信息
                logging.info(u"[+] {} find Apache ActiveMQ Console控制台弱口令".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info(u"[-] {} do not found Apache ActiveMQ Console控制台弱口令".format(e))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info(u"[-] {} do not found Apache ActiveMQ Console控制台弱口令".format(e))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
