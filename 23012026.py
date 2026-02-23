mylist = [x*x for x in range(1, 21) if x%2 == 0]

print(mylist)

fruits = ["Apple", "Banana"]
fruits = [i.upper() for i in fruits]

print(fruits)

#aliasing of lists

x = [10, 20, 30]
y = x
print(x, id(x))
print(y, id(y))
x[2] = 99
y[2] = 10
print(x, id(x))
print(y, id(y))

#use y = x[:] to get diffrent storage in lists

