import read_file
import gc_con

# Step 1: Read DNA sequence from file
dna_sequence = read_file.read_dna_from_file("dna_sequence.txt")

# Step 2: Calculate GC content
gc_content = gc_con.calculate_gc_content(dna_sequence)

# Step 3: Print and save the result
print(f"DNA Sequence: {dna_sequence}")
print(f"GC Content: {gc_content}%")

with open("gc_content.txt", "w") as file:
    file.write(f"GC Content: {gc_content}%")

print("GC content saved to gc_content.txt")
