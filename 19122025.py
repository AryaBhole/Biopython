#Motif Checker

# x = input("Enter a nucleotide sequence : ")

# print(f"Number of A in sequence : {x.count("A")}")
# print(f"Number of T in sequence : {x.count("T")}")
# print(f"Number of G in sequence : {x.count("G")}")
# print(f"Number of C in sequence : {x.count("C")}")

# print(f"The total length of the input sequence is : {len(x)}")

# s = "PALYDEHRDSETLY"
# m = "HRD"

# count = 0
# for y in range(len(s)):
#     if m[0] == s[y] and m[1] == s[y + 1] and m[2] == s[y + 2] and y + 1 < len(s) :
#         count += 1

# if count > 0:
#     print("Motif is present in the sequence")

seq = input("Enter a sequence : ").upper()
mot = input("Enter the motif : ")

f = False
a = 0

for x in range(len(seq)):
    part = seq[a : a + len(mot)]
    if part == mot:
        f = True
        print(f"Motif is present in the sequence at {a+1} position")
    a += 1

if f != True:
    print("Motif is not present in the sequence")