#encoding:utf-8
try:
    import os
    from ftplib import FTP
    import logging
    import sys
    import re
except:
    os._exit(6)

logging.basicConfig(level=logging.DEBUG,format='%(message)s')
def check(hostname,port):
    try:
        f = FTP()
        #port = '21'
        version = f.connect(hostname,port,timeout=1)
        Is_true = re.search("2.3.4",version).group()
    except Exception as e:
        logging.info("[*] time out")
        return 4
    try:
        # logging.info('[*] ' + str(hostname) + " FTP Anonymous login successful!")
        if Is_true:
            logging.info("[+] {} find Vsftp".format(ip))
            return 1
        else:
            logging.info("[-] {} do not found Vsftp".format(ip))
            return 2
    except Exception as e:
        logging.info("[*] Somethong Error!!")
        return 3
def main(ip,port):
    get = check(ip,int(port))
    os._exit(get)
if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))
    