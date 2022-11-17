try:
    import socket,os,logging,binascii,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)
def check(ip,port):
    try:
        data = b"3039020112633404000a01000a0100020203e8020100010100870b6f626a656374636c61737330130411737562736368656d61537562656e747279"
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((ip,port))
        s.send(binascii.a2b_hex(data))
        get = s.recv(4096)
        if get:
            if b"authentication required" in get:
                logging.info("[-] {} do not found idap unauthorized".format(ip))
                os._exit(1)
            else:
                logging.info("[+] {} find idap unauthorized".format(ip))
                os._exit(2)
        else:
            logging.info("[+] {} find idap unauthorized".format(ip))
            os._exit(2)   
    except Exception as e:
        logging.info("[*] {}".format(e))

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,int(port))