# def fact(num):
#     if(num==0 or num==1):
#         return 1
#     else:
#         return fact(num-1)*num
    

# print(fact(4))

def cal_num(n):
    if(n==0):
        return 0
    return cal_num(n-1) + n

print(cal_num(5))


# def print_list(list,idx):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)


# fruits=["mango","litchi","banna"]
# print_list(fruits,0)
    