#encoding:utf-8
try:
    import os
    import socket
    import logging
    import re
    import binascii
except:
    os._exit(6)

logging.basicConfig(level=logging.INFO,format='%(message)s')
def check(ip,port):

    data = b"00680000010000000136012c000008007fff7f0800000001002e003a0000000000000000000000000000000034e600000001000000000000000028434f4e4e4543545f444154413d28434f4d4d414e443d736572766963655f72656769737465725f4e5347522929"
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip,port))
    except:
        logging.info("[*] time out")
        return 4
    try:
        s.send(binascii.a2b_hex(data))
        get = s.recv(4096)
        if (re.search("DESCRIPTION",get).group(0)):
            logging.info("[+] {} find oracle Tns middleman poisoning".format(ip))
            return 1
        
        logging.info("[-] {} do not found Tns middleman poisoning")
        return 2
    except Exception as e:
        logging.info("[*] Something Error!!")
        return 3
def main(ip,port):
    get =  check(ip,port)
    os._exit(get)

if __name__ =="__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))