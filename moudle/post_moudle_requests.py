#encoding:utf-8
try:
    import requests,os,sys,logging
    requests.packages.urllib3.disable_warnings()
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(url):
    
    payload = "                 "                                   #填写payload
    header = {
        
    }                                                               #填写header头
    data = "        "                                               #填写data数据
    try:
        req = requests.post(url+payload,headers=header,data=data,timeout=3,verify=False,allow_redirects=False)

        if req.status_code == 200:
            if ('    ' in req.text) and  (''    ' in req.text) and ('     ' in req.text):              #填写判断条件
                logging.info("[+] {} find            ".format(ip))                          #填写漏洞名
                os._exit(1)

        logging.info("[-] {} do not found            ".format(ip))                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__ == "__main__":
    url = sys.argv[1]
    check(url)