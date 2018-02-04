import time
from datetime import datetime as dt

host_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect ="127.0.0.1"
website_list=["www.washingtonpost.com", "washingtonpost.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours...")
        with open(host_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content: #if we are in working hours and the websites are present, the program will move on
                    pass
                else:
                    file.write("\n" + redirect + " " + website + "\n")
    else:
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print("Fun Time")
    time.sleep(5)
