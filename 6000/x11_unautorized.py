#encoding:utf-8
try:
    import os
    import socket
    import binascii
    import logging
    import time
except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')
def check(ip,port):
    data = b'6c000b000000000000000000'
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip,port))
    except Exception as e:
        logging.info("[*] time out")
        return 4
    try:
        s.send(binascii.a2b_hex(data))
        time.sleep(0.1)
        get = s.recv(4096)
        if b"X.Org" in get:
            logging.info("[+] {} find x11 unauthorized".format(ip))
            return 1
        logging.info("[-] {} do not found x11 unauthorized".format(ip))
        return 2
    except Exception as e:
        logging.info("[*] Something Error!!")
        return 3

def main(ip,port):
    get =  check(ip,port)
    os._exit(get)
if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))