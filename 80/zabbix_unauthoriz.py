try:
    import os,logging,requests,sys
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*]{}".format(e))

def check(ip,port):
    check_paths = ["/zabbix.php?action=problem.view&ddreset=1","/overview.php?ddreset=1","/srv_status.php?ddreset=1","/latest.php?ddreset=1",]
    for path in check_paths:
        try:    
            target = "http://" + ip + ":" +port + path
            req = requests.get(target,timeout=3,allow_redirects=False)
            if req.status_code == 200:
                logging.info("[+] {} find zabbix unauthorize".format(ip))
                os._exit(1)
        except :
            pass
    logging.info("[-] {} do not found zabbix unauthorized".format(ip))
    os._exit(2)


if __name__ == "__main__":
        ip = sys.argv[1]
        port =sys.argv[2]
        check(ip,port)