# f=open("D:\Python\Programe\FileI\FileI\demo.txt", "r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()


# f=open("D:\Python\Programe\FileI\FileI\demo.txt", "w")
# f.write("I am reading python. 123")
# f.close()

# f=open("D:\Python\Programe\FileI\FileI\demo.txt", "a")

# f.write("\nI will move to react js")
# f.close()


# f=open("Sample.txt","w")
# f.close()

# with open("D:\Python\Programe\FileI\FileI\demo.txt","r") as f: 
#     data=f.read()
#     print(data)
#     f.close()

# with open("D:\Python\Programe\FileI\FileI\demo.txt","w") as f: 
#     f.write("new data")

# import os
# os.remove("D:\Python\Programe\FileI\FileI\demo.txt")


# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("Java","python")
# print(new_data) 


# with open("practice.txt","w") as f:
#     f.write(new_data)



# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find("learning") !=-1):
#         print("found")
#     else:
#         print("not found")



# def check_for_line():
#     word="learning"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word  in data):
#                 print(line_no)
#             line_no+=1
#     return -1
# check_for_line()

with open("practice.txt","r") as f:
    data = f.read()
    print(data)

    count=0
    nums = data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1

print(count)