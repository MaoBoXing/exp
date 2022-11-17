#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import requests
    import base64
    import sys
    import os
    import logging
    logging.basicConfig(level=logging.INFO,format='%(message)s')
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)
password_base64 = []
find_user_passw = []
is_true = False
def get_cheek_pass():
    names = ["admin","role","role1","root","tomcat","both"]
    passwds = ["j5Brn9","admin","tomcat","changethis","role1","root","123456"]
    
    for name in names:
        for password in passwds:
            #logging.info(password.strip())
            pass_str = name.strip()+":"+password.strip()
            #logging.info(pass_str)
            base64_str = base64.b64encode(pass_str.encode('utf-8')).decode("utf-8")
            #logging.info(base64_str)
            password_base64.append(base64_str)
                    
def check_path(ip,port):
    targets = "http://" + ip +":" + port
    paths = ["/manager/status","/manager/html","/admin/j_security_check"]
    for path in paths:
        try:
            resp = requests.get((targets+path),timeout=2,verify=False)
            if resp.status_code == 401:
                return path
        except Exception as e:
            pass
    logging.info("[-] {} do not found tomcat weak passwd".format(ip))
    os._exit(2)
def cheek_tomcat(ip,port,path):
    global is_true,find_user_passw
    url = "http://"+ip + ":" + port + path
    i = 0
    con = int(len(password_base64))
    for basic in password_base64:
        i = i + 1
        # logging.info("[+] 正在进行第 {} 组密码暴破## 已完成: {:.2f}%".format(i,i/con),end="\r")
        #logging.info(basic)
        headers = {
        "Accept":"application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*",
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", 
        "Content-Type":"application/x-www-form-urlencoded",
        'Authorization': 'Basic %s' % basic
        }
        try:
            req = requests.get(url, headers=headers, timeout=5,verify=False)
            if req.status_code != 401:
                is_true =True
                find_user_passw.append(base64.b64decode(basic.encode("utf-8")).decode("utf-8"))
                req.close()
            else:
                pass
        except Exception as e:
            logging.info(e)




if __name__ == "__main__":
    get_cheek_pass()

    ip = sys.argv[1]
    port = sys.argv[2]
    path = check_path(ip,port)
    cheek_tomcat(ip, port,path)
    if is_true:
        logging.info("[+] {} find tomcat weak passwd :{}".format(ip,find_user_passw))
        os._exit(1)
    logging.info("[-] {} do not found tomcat weak passwd".format(ip))
    os._exit(2)