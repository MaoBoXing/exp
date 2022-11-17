#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
    requests.packages.urllib3.disable_warnings()
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payload = "/graph_realtime.php?action=init"                                                      #填写payload
    payload1 = "/poller_realtime.php"
    try:
        tar = "https://" + ip + ":" + port 
        ssl = requests.session()
        req = ssl.get(url = tar+ payload,timeout=3,verify=False,allow_redirects=False)
        if req.status_code == 200:                                                          #修改匹配返回代码
            req1 = ssl.get(tar+ payload1,timeout=3)
            if req1.status_code == 200:
                
                logging.info("[+] {} find Cacti_Weathermap_File_Write".format(ip))                                 #填写漏洞信息
                os._exit(1)
        
        logging.info("[-] {} do not found Cacti_Weathermap_File_Write".format(ip))                             #填写漏洞信息
        os._exit(2)
    except Exception as e:
        logging.info("[*] timeout")
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
