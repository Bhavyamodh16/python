int =2
print(int,type(int),"\n")
a=22.4
print(a,type(a),"\n")
c="bhavya"
stri=str(123)
print(c,type(c),"\n")
print(type(stri)) #this is used for converting integer to string
d=True
print(d,type(d),"\n")
e=["ramesh",2]
e.append("sushma")
print(e,"\n")
e.insert(0,"bhavesh")
print(e,"\n")
e.pop(1)
print(e)
print(e,type(e),"\n")
f=("ramesh",2,"ramesh")
print(f,type(f),"\n")
g={"name":"Bhavya","surname":"Modh"}
print(g["name"])
print(g["surname"])
# h=set()
h={"babes",3,"linkesh"}
print(h,type(h),"\n")
print("\n")
print(len("hello bhavya")) #returns the number of elements in an object means how many words are there hello=5 bhavya=6 and one space
print("HELLO".lower()) #this makes the string upper all cases same for lower ig
ind=["hello"]
print(ind[1]) #index this process is indexing h=0 e=1
print(ind.index("hello"))
ind[0]="B" #this throws an error bcz list is immutable
change_string=["h","e","l","l","o"]
change_string[3]="p"
print(change_string)
