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
        get = binascii.b2a_hex(s.recv(4096))
        if get:
            succeed = get[:2]
            if succeed == '01':
                logging.info("[+] find x11 unauthorized")
                os._exit(1)
            else:
                logging.info("[-] do not found x11 unauthorized")
                os._exit(2)
        else:
            logging.info("[-] do not found x11 unauthorized")
            os._exit(2)
    except Exception as e:
        logging.info("[*] Something Error!!")
        os._exit(3)

def main(ip,port):
    get =  check(ip,port)
if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))