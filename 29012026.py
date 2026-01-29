#tuple string dict

s = "hello"
t1 = tuple(s)
t2 = tuple([s])
print(t1)
print(t2)

dict = {
    "username" : "raju",
    "uni" : "nit",
    "city" : "vizag"
}

print(dict)
# no indexes only key value pairs #dict[2] will give error

print(dict.pop("uni"))
print(dict.popitem())

#dict.update(r1 : r2)