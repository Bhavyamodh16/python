# import os

# print(os.listdir()) #this will list all files in a folder

# os.mkdir("sample.py") #this is used to make a folder/directory
# os.remove("xxx.txt") #it is used to delete a file folder cant be deleted

import subprocess
result=subprocess.run(args=["ls"],capture_output=True, text=True)
print(result.stdout)

subprocess.run(["echo","hello"])

process = subprocess.Popen(args=["ping","www.google.com"],stdout=subprocess.PIPE, text=True)
oo=subprocess.Popen(["nmap","-sS","192.168.1.1"])
for line in process.stdout:
        print(line.strip())