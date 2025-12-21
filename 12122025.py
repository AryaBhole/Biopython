# print("These are even numbers in (1, 20) : ")
# for x in range(2, 21, 2):
#     print(x)

# print()

# print("These are odd numbers in (1, 20) : ")
# for x in range(1, 20, 2):
#     print(x)

# x = int(input("Enter a number : "))

# for y in range(1, x + 1):
#     print()
#     for z in range(1, 11):
#         print(f"{y} * {z} = {z * y}")

x = int(input("Enter a number : "))

for y in range(1, 11):
    print()
    for z in range(1, x + 1):
        print(f"{z} * {y} = {z * y}", end = "\t")