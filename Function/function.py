# sum
# def cal_sum(a,b):
#     sum = a + b
#     return sum


# num = cal_sum(10,20)
# print(num)


# Average
# def avg(a,b,c):
#     num=int((a+b+c)/3)
#     return num


# output = avg(5,6,9)
# print(output)

# default value
# def cal_prod(a,b=2):
#     print(a *b)
#     return a*b
# cal_prod(2)

# cities = ["delhi","grgone","pune"]


# def print_len(list):
#     print(len(list))


# print_len(cities)


# cities = ["delhi","grgone","pune"]
# def print_mylist(list):
#     for item in list:
#         print(item , end =" ")

# print_mylist(cities)

# def fac(n):
#     fac=1
#     for a in range(1,n+1):
#         fac=fac*a
#     print(fac)

# fac(5)

# def converter(usd_val):
#     inr_val = usd_val*83
#     print(usd_val,"USD =",inr_val,"INR")

# converter(2)


# Odd & Even
def odd_even():
    num=int(input("enter a number : "))
    if(num%2==0):
        print("even")
    else:
        print("odd")


odd_even()
