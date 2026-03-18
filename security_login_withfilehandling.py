with open("file.txt","r")as file:
    read=file.read()
    username=read.split()
def login(loginlist,user):
    counter=0
    for i in loginlist:
        if i==user:
            counter =counter+1
    if counter>=2:
        print("you have been locked")
    else:
        print("you can log in")
login(username,"suman")
    
    
    
