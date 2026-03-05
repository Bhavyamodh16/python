fruits="apple","banana","cherry"
for fruit in fruits:
    print(fruit)

print("\n","for loop")
for i in range(1,10):
    print(i)

print("\n","while loop")
count=0
while count <=5:
    
    count+= 1
    print("\n",count)

print("for loop with break starts")
for f in range(1,11):
    if f==5:
        break
    # elif f%2==0:
    #     continue
    print("\n",f,"\n")
    
for i in range(5):
    for j in range(3):
        print(i,j)