# balance = int(input("Enter your current balance: "))
# task = input("Withdrawl or Deposit : ")
# amount = int(input("Enter amount : "))

# if task == "Withdrawl" and amount < balance:
#     balance -= amount
#     print(f"New balance : {balance}")
# elif task == "Deposit":
#     balance += amount
#     print(f"New balance : {balance}")
# else:
#     print("Enter a valid option")

def add (a, b):
    return a + b, a * b

a = int(input("Enter a : "))
b = int(input("Enter b : "))

print(add(a, b))

#https://www.w3schools.com/python/python_lists_comprehension.asp