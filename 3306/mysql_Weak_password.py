#encoding:utf-8
try:
    import os
    import pymysql.cursors
    import sys
except:
    os._exit(6)
def check(ip,port):
    mysql_username = ["root", "admin", "user"]
    common_weak_password = ["root","123456","test","root","admin"]

    for username in mysql_username:
        for password in common_weak_password:
            try:
                mydb = pymysql.connect(
                host=ip ,
                port = port,
                user=username,   
                passwd=password,
                # timeout=1
                )
                mycursor= mydb.cursor()  
                mycursor.execute("SHOW DATABASES")  
                result = mycursor.fetchall()  
                mydb.close() 
                if result:
                    print("[+] {} find mysql weak password".format(ip))
                    return 1                
            except Exception as e :
                print(e)
                pass
    print("[-] {} do not found mysql weak password".format(ip))
    return 2
def main(ip,port):
    get =  check(ip,port)
    os._exit(get)

if __name__ =="__main__":
    import sys
    ip = sys.argv[1]
    port = sys.argv[2]
    main(ip,int(port))