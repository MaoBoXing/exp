#encoding:utf-8
try:
    import os
    import socket
    import binascii
    import logging
    import struct
    import re
except Exception as e:
    os._exit(6)

logging.basicConfig(level=logging.INFO,format='%(message)s')
def check(ip,port):
    data_get_port = b"623ad0b60000000000000002000186a0000000020000000300000000000000000000000000000000000186a5000000030000000600000000" 
    data_1 = b'800000445f862cce0000000000000002000186a50000000300000005000000010000001c623293a9000000046b616c69000003e8000003e800000001000003e80000000000000000'
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.settimeout(1)
        connect = (ip,port)
    except:
        logging.info("[*] first time out")
        return 4
    try:
        s.sendto(binascii.a2b_hex(data_get_port),connect)
        get_port = s.recvfrom(4096)[0]
        port1 = re.search("(....)$",get_port).group(1)
        port1_int = struct.unpack('>I',port1)[0]
        s.close()
    except Exception as e:
        logging.info("[*] Something Error!!")
        return 3
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((ip,port1_int))
    except Exception as e :
        logging.info("[-] {} do not found show mount".format(ip))
        return 2
    try:
        s.send(binascii.a2b_hex(data_1))
        get = binascii.b2a_hex(s.recv(4096))
        if re.search("2a000000",get).group(0):
            logging.info("[+] {} find Showmount -e".format(ip))
            return 1
        logging.info("[-] {} do ot found Showmount -e".format(ip))
        return 2
    except Exception as e:
        logging.info("[*] Something Error!!")
def main(ip,port):
    get = check(ip,port)
    os._exit(get)
if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))