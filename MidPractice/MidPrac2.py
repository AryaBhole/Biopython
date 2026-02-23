#Creating a file which creates a text file to store a random dna sequence

import random 

def makeDna (length):
    bases = ['A', 'T', 'G', 'C']
    dna = ''.join(random.choices(bases, k = length))
    return dna

with open ("new.txt", "w") as file:
    file.write(makeDna(10))

with open ("new.txt", "r") as file:
    seq = file.read()

def getCom (seq):
    map = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
    return ''.join(map[base] for base in seq)

rev = getCom(seq)[::-1]

with open ("new2.txt", "w") as file:
    file.write("Random DNA : \n")
    file.write(seq + "\n \n")
    file.write("Complement : \n")
    file.write(getCom(seq) + "\n \n")
    file.write("Rev Complement : \n")
    file.write(rev)