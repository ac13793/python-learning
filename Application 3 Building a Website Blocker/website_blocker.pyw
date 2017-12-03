import time
from datetime import datetime as dt

#hosts_path = r"C:\\WINDOWS\\System32\\drivers\\etc\\hosts"
hosts_path = "hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "gmail.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("Working hours.....")
        # Access hosts file and update it
        # hosts file can only be accessed by the administrator
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fun hours....")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            # Read the file content and move pointer at the beginning of the file
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    # Write all lines except those are in website list
                    file.write(line)
            # Once we have written all the content except websites added in the last
            # Truncate the content i.e old content with website lines
            file.truncate()
    time.sleep(5)
