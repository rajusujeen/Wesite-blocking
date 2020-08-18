import time
from datetime import datetime as dt
# windows host file llocation
hostspath=r"c:\Windows\System32\Drivers\etc\hosts"
redirect="127.0.0.1"
# Add the website you want to block in the folloeing block
websites=["www.youtube.com","youtube.com"]
print(dt.now().year,dt.now().month,dt.now().day,9)

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,21):
        print ("sorry this website was blocked by vedanth")
        with open(hostspath,'r+') as file:
            content=file.read()
            for site in websites:
                    if site in content:
                        pass
                    else:
                        file.write(redirect+" "+site+"\n")
    else:
        with open(hostspath,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
            file.truncate()
        print ("Access allowed by vedanth!")
    time.sleep(5)                
