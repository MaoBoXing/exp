import os,re
def get_ip():
    ips_file = open("ips.txt","r")
    ip_ports = []
    for ip in ips_file:
        re_result = re.search("://(.*)?:(.*)",ip)
        re_ip = re_result.group(1)
        re_port = re_result.group(2)
        ip_ports.append({re_ip.strip():re_port.strip()})
    return ip_ports

    
def main(poc_name,dport):
    ip_port_dic = get_ip()
    ip_find_dic = []
    print(ip_port_dic)
    for ip in ip_port_dic:
        # print(type(str(ip.keys()) ))
        print("python " + poc_name+" " + ip.keys()[0] +" " +ip.values()[0])
        p = os.system("python " + poc_name+" " + ip.keys()[0] +" " +ip.values()[0])
        if  p == 1:
            ip_find_dic.append(ip.keys()[0] +" " +ip.values()[0])
    print("\nfind:"  )
    print(ip_find_dic)
    file = open("find_ip.txt","w")
    file.writelines(ip_find_dic)

if __name__=="__main__":
    import sys
    
    
    pocname = sys.argv[1]
    port = sys.argv[2]
    main(pocname,port)