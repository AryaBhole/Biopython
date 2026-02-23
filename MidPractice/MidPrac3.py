#count GC content in a file with random DNA

import random

def makeDna (length):
    bases = ['a', 't', 'g', 'c']
    return ''.join(random.choices(bases, k = length))

def countGC (seq):
    G = seq.count('g')
    C = seq.count('c')
    if len(seq) == 0:
        return -1
    return (G + C) * 100 / len(seq)

with open ("new3.txt", "w") as file:
    file.write(makeDna(10))

with open ("new3.txt", "r") as file:
    seq = file.read()

with open ("new4.txt", "w") as file:
    file.write(seq + "\n \n")
    file.write("GC Content : " + str(countGC(seq)))