# 1
count=1
while count<=5 :
    print("hellow")
    count+=1
    
# 2
i=1
while i<=100 :
    print(i)
    i+=1

# 3
i=100
while i>=1 :
    print(i)
    i-=1

# 4
i=1
while i<=10 :
    print(3*i)
    i+=1

# 5
num=[1,4,9,16,25,36,49,64,81,100]
i=0
while i < len(num) :
    print(num[i])
    i+=1



# 6
num =(1,4,9,16,25,36,49,64,81,100)
i=0
x=36
while i<len(num) :
    if(num[i]==x):
        print("found at index",i)
        break
    else:
        print("finding....")
    i+=1

# 7
i=1
while i<=5 :
    print(i)
    if(i == 3):
        break
    i+=1
print("end of loop")    

# 8
i=0 
while i<=5 :
    if(i==3) :
        i+=1
        continue
    print(i)
    i+=1


