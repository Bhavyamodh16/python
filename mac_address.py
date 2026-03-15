# import subprocess
# subprocess.run(["macchanger","-m","fc:e5:57:12:a1:a6","eth0"])

ip=["192.168.xx.xx","192.168.xx.xx","198.168.xx.xx","197.168.xx.xx"]
network=[]
for address in ip:
    network.append(address[0:3])
print(network)
