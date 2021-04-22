# a = ["*", "*", "*"]
# b = ["*", "*", "*", "*", "*"]

# for i in range(3):
#     print(i, end="")
# print("*")

# for i in range(3):
#     for j in range(i):
#         print(i, end="")
#     print("*")

# for i in range(3):
#     for j in range(3-i):
#         print(" ", end="")
#     print("*")

for i in range(3):
    for j in range(3-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    for j in range(i):
        print("*", end="")
    print("*")

# year = 2000

# if(year%4==0):
#     if(year%100==0):
#         if(year%400==0):
#             print("{0} is a leap year".format(year))
#         else:
#             print("{0} is not a leap year".format(year))
#     else:
#         print("{0} is a leap year".format(year))
# else:
#     print("{0} is not a leap year".format(year))