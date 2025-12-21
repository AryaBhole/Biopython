# for i in range(5, 0, -1):
#     for x in range(i, 5):
#         print("*", end = "")
#     print()

# for i in range(1, 5):
#     for j in range(0, i):
#         print("*", end = "")
#     print()

x = int(input("Enter a number : "))

i = 1
while i < 11:
    print(f"{x} * {i} = {x * i}")
    i += 1