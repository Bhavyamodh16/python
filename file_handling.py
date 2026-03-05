with open("sample.txt","w")as file:
    file.write("hello,this is a created  file by python.\n")
with open("sample.txt","a") as file:
    file.write("this is second line.\n")    
with open("sample.txt","r") as file:
    print(file.read())
with open("sample.txt","r+")as file:
    file.write("using r+ write and read.\n")
    file.seek(0)
    print(file.read())
