#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:No.2768
try:
    import requests
    import sys
    import os
    import logging
    logging.basicConfig(level=logging.INFO,format='%(message)s')
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)
# test_Path = ["/swagger"]
user_passw = []
Url_Paths = ["/jmx-console", "/web-console", "/jbossws", "/admin-console"]
UserNames = ["admin", "jboss", "manager", "vulhub"]
PassWords = ["admin", "jboss", "manager", "123456", "vulhub"] 

def Brust1(Url0):
    try:
        global user_passw
        for i in Url_Paths:
            Url1 = Url0 + i
            # logging,info(Url1)
            for u in UserNames:
                for p in PassWords:
                    req0 = requests.get(Url1)
                    if req0.status_code == 401:
                        req1 = requests.get(Url1, auth=(u, p))
                        if req1.status_code == 200:
                            user_passw.append({Url1:{u:p}})
                            
                            break
        if user_passw:
            logging.info("[+] Found Weak password:"+ str(user_passw))
            os._exit(1)
        logging.info("[-] {} do not found weak passwd".format(Url0))
        os._exit(2)
    except Exception as e:
        logging.info(e)
        os._exit(3)

if __name__ == "__main__":
    Ip_Addr = sys.argv[1]
    Port = sys.argv[2]
    Url0 = "http://" + Ip_Addr + ":" + Port
#    logging.info(Url0)
    Brust1(Url0)