#encoding:utf-8
try:
    import os
    import socket
    import logging
    logging.basicConfig(level=logging.INFO,format='%(message)s')
    import binascii
    import time
except:
    os._exit(6)
def check(ip,port):
    data = b'656e76690a'
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(20)
        s.connect((ip,port))
    except :
        logging.info("[*] time out")
        return 4
    try:
        s.send(binascii.a2b_hex(data))
        time.sleep(0.1)
        get = s.recv(4096)
        if b'zookeeper' in get:
            logging.info("[+] {} find zookeeper unauthorized".format(ip))
            return 1
        logging.info("[-] {} do not found zookeeper unauthorized".format(ip))    
        return 2
    except Exception as e:
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