import random

def generateDna(length):
    bases = ['A', 'T', 'G', 'C']
    return ''.join(random.choices(bases, k = length))

with open("randomDNA2.txt", "w") as file:
    file.write(generateDna(10) + "")

# def readDNA(length):
#     return file.read().strip().replace("\n", "").upper()

# def complementDNA(dna_seq):
#     complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
#     return ''.join(complement_map[base] for base in dna_seq)

def complement_dna(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in sequence)

def reverse_complement_dna(sequence):
    return complement_dna(sequence)[::-1]

with open("randomDNA2.txt", "r") as file:
    dna_sequence = file.read().strip().upper()

complement_sequence = complement_dna(dna_sequence)
reverse_complement_sequence = reverse_complement_dna(dna_sequence)

with open("output_randomDNA2.txt", "w") as file:
    file.write("Original Sequence:\n" + dna_sequence + "\n\n")
    file.write("Complement Sequence:\n" + complement_sequence + "\n\n")
    file.write("Reverse Complement Sequence:\n" + reverse_complement_sequence)

print("Processing complete. Output saved in output_randomDNA2.txt")
