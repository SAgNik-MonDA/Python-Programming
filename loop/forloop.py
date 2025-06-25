# 1
list= [1,2,3,4,5]
for a in list :
    print(a)

# 2
list = [1,4,9,16,25,36,49,64,81,100]
for a in list :
    print(a)

# 3
tuple=(1,4,9,16,25,36,49,64,81,100)
x=16
i=0
for b in tuple :
    if(b == x) :
        print("element found",i)
        break
    i+=1

# 4
a=int(input("enter a number : "))
for i in range(1,11) :
    print(a*i)

# 5
n=5
sum=0
for a in range(n+1) :
    sum=sum+a
print(sum)

factorial

# 6
n=5
fact=1
for a in range(1,n+1) :
    fact=fact*a
    a+=1
print(fact)