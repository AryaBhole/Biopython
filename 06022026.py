import re

proteinSeq = "QWERTYUIOPQWER"
motif = "QWE"

print(re.search(motif, proteinSeq))
print(re.findall(motif, proteinSeq))
print(re.finditer(motif, proteinSeq))

for match in re.finditer(motif, proteinSeq):
    print("Match : ", match.group(), "Start : ", match.start() + 1, "End : ", match.end())

import calc
#from calc import * or add

a = 5
b = 7

print(calc.add(a, b))

import random

def generateDna(length):
    bases = ['A', 'T', 'G', 'C']
    return ''.join(random.choices(bases, k = length))

print(generateDna(10))

with open("randomDNA.txt", "w") as file:
    for i in range(5):
        file.write(generateDna(10) + "\n")

print("DNA sequences saved in new text file")