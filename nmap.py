import subprocess
print("enter the ip addr \n")
ip=input()
print("enter the port \n")
port=input()
subprocess.run(["nmap","192.168.121.128","-p","8383","-sT","-sV","-O"])