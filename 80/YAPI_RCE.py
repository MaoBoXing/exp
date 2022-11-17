#encoding:utf-8
try:
    import requests,os,sys,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "http://" + ip + ":" + port
    payload = "/api/user/reg"                                   #填写payload
    
    try:
        req = requests.post(url=target+payload,timeout=3,verify=False,allow_redirects=False)

        if req.status_code == 200:
            if (b'禁止注册，请联系管理员' not in req.text) and  (b'邮箱不能为空' in req.text):              #填写判断条件
                logging.info("[+] {} find YAPI_RCE".format(ip))                          #填写漏洞名
                os._exit(1)

        logging.info("[-] {} do not found YAPI_RCE".format(ip))                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] timeout")
        os._exit(4)

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)