import subprocess
print("enter the ip addr \n")
ip=input()
print("enter the port \n")
port=input()
scan=(input("enter scan type \n 1=SYN Scan \n 2=TCP Scan\n"))
if scan==1:
    subprocess.run(["nmap","192.168.121.128","-p","8383","-sS","-sV","-O"])
else:
    subprocess.run(["nmap","192.168.121.128","-p","8383","-sT","-sV","-O"])
    