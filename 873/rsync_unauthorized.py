#encoding:utf-8
try:
    import os
    import logging
    import time
    import re
    import socket
    import binascii
except:
    os._exit(6)

logging.basicConfig(level=logging.INFO,format='%(message)s')
def check(ip,port):
    data1 = b'405253594e43443a2033312e300a'
    data2 = b'0a'
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(20)
        s.connect((ip,port))
    except Exception as e:
        logging.info("[-] {} time out".format(ip))
        return 4
    try:
        s.send(binascii.a2b_hex(data1))
        s.recv(4096)
        s.send(binascii.a2b_hex(data2))
        get = re.search("(?<=^).*?(?=(20))",binascii.b2a_hex(s.recv(4096))).group(0)+"0a"
        s.close()
        
    except Exception as e:
        logging.info("[-] Something Error!!")
        return 3
    
    time.sleep(0.1)
    try:
        s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s1.settimeout(1)
        s1.connect((ip,port))
    except:
        logging.info("[-] {} time out".format(ip))
        return 4
        
    try:
        s1.send(binascii.a2b_hex(data1))
        s1.recv(4096)
        s1.send(binascii.a2b_hex(get))
        time.sleep(0.1)
        get2 = s1.recv(4096)
        if b'OK' in get2:
            logging.info("[+] {} find rsync unauthorized".format(ip))
            return 1
        logging.info("[-] {} do not found rsync unauthorized".format(ip))
        return 2
    except Exception as e:
        logging.info("[-] {} somethong error!!".format(ip))
        return 3





def main(ip,port):
    get =  check(ip,port)        
    os._exit(get)
    
if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))