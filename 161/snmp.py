#encoding:utf-8
try:
    import os 
    import socket
    import logging
    import binascii
except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')

def check(ip,port):
    data_public_private = [b"302a020100040770726976617465a01c0204fffffffe020100020100300e300c06082b060102010101000500",b"302902010004067075626c6963a01c0204ffffffff020100020100300e300c06082b060102010101000500", ]
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.settimeout(1)
        connect = (ip,port)
    except Exception as e:
        return 3
    for data in data_public_private:
        try:
            s.sendto(binascii.a2b_hex(data),connect)
            get = s.recvfrom(4096)
            if "public" in get[0] or "private" in get[0]:
                return 1
        except Exception as e:
            pass
    return 2
def main(ip,port):
    get = check(ip,port)
    if get == 1:
        logging.info("[+] {} find snmp default community name".format(ip))
    elif get == 2:
        logging.info("[-] {} do not found snmp default community name".format(ip))
    else:
        logging.info("[*] somthing error!!")
    os._exit(get)

if __name__ =="__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))