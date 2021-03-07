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