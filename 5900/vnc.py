#encoding:utf-8
try:
    import os
    import socket
    import binascii
    import time
    import logging
    import re
except:
    os._exit(6)

logging.basicConfig(level=logging.INFO,format='%(message)s')
def check(ip,port):
    data = b'524642203030332e3030310a'
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip,port))
    except Exception as e:
        logging.info("[*] {} time out".format(ip))
        return 4
    try:
        s.send(binascii.a2b_hex(data))
        time.sleep(1)
        get = s.recv(4096)
        version = re.search("RFB.00(.).00(.)",get)
        vnc_version = float(version.group(1) + '.'+version.group(2))
        if vnc_version <=3.7:        
            if binascii.a2b_hex(b'00000001') in get:
                logging.info("[+] {} find vnc unauthorized".format(ip))
                return 1
        logging.info("[-] {} do not found vnc unauthorized".format(ip))    
        return 2
    except Exception as e:
        print(e)
        logging.info("[*] Something Error!!")
        return 3




def main(ip,port):
    get = check(ip,port)
    os._exit(get)
if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))