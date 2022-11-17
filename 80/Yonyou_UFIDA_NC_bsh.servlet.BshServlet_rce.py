#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payload = "/servlet/~ic/bsh.servlet.BshServlet"                                                      
    try:
        tar = "http://" + ip + ":" + port
        req = requests.get(tar + payload,timeout=3,verify=False,allow_redirects=False)
        if req.status_code == 200:                                                          
            if ( b"BeanShell" in req.text ):          
                logging.info(u"[+] {} find Yonyou_UFIDA_NC_bsh.servlet.BshServlet_rce".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info(u"[-] {} do not found Yonyou_UFIDA_NC_bsh.servlet.BshServlet_rce".format(ip))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info(u"[-] {} do not found Yonyou_UFIDA_NC_bsh.servlet.BshServlet_rce".format(ip))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] timeout")
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
