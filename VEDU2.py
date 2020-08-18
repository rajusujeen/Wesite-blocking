import time 
import datetime  
  
host_path = r"c:\Windows\System32\Drivers\etc\hosts"  
redirect = "127.0.0.1"  
websites = ["www.facebook.com", "https://www.facebook.com"]  
  
while True:  
    if datetime(datetime.now().year,datetime.now().month,datetime.now().day,9)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,17):  
        with open(host_path,"r+") as fileptr:  
            content = fileptr.read()  
            for website in websites:  
                if website in content:  
                    pass  
                else:  
                    fileptr.write(redirect+"        "+website+"\n")  
    else:  
        with open(host_path,'r+') as file:  
            content = file.readlines();  
            file.seek(0)  
            for line in content:  
                if not any(website in line for website in               websites):  
                    file.write(line)  
            file.truncate()  
    sleep(5)  