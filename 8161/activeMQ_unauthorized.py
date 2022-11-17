try:
    import socket
    import os
    import logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
    import binascii
except Exception as e:
    logging.info("[*]{}".format(e))
    os._exit(6)
def check(ip,port):
    data = b'474554202f61646d696e2f20485454502f312e310d0a486f73743a203139382e3132302e302e34323a383136310d0a557365722d4167656e743a204d6f7a696c6c612f352e30202857696e646f7773204e542031302e303b2057696e36343b207836343b2072763a3130302e3029204765636b6f2f32303130303130312046697265666f782f3130302e300d0a4163636570743a20746578742f68746d6c2c6170706c69636174696f6e2f7868746d6c2b786d6c2c6170706c69636174696f6e2f786d6c3b713d302e392c696d6167652f617669662c696d6167652f776562702c2a2f2a3b713d302e380d0a4163636570742d456e636f64696e673a20677a69702c206465666c6174650d0a4163636570742d4c616e67756167653a207a682d434e2c7a683b713d302e382c7a682d54573b713d302e372c7a682d484b3b713d302e352c656e2d55533b713d302e332c656e3b713d302e320d0a417574686f72697a6174696f6e3a204261736963205957527461573436595752746157343d0d0a557067726164652d496e7365637572652d52657175657374733a20310d0a0d0a'
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((ip,port))
        s.send(binascii.a2b_hex(data))
        get = s.recv(4096)
    except Exception as e:
        logging.info("[*] {} find activeMQ unauthorized".format(ip))
        os._exit(4)

    if b" 200 OK" in get:
        logging.info("find")
        os._exit(1)
    else:
        logging.info(" do not found")
        os._exit(2)



if __name__=="__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,int(port))