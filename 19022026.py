# Import required modules (if needed)

def read_dna_from_file(filename):
    """Reads a DNA sequence from a file."""
    with open("random_dna.txt", "r") as file:
        return file.read().strip().replace("\n", "").upper()


# Standard Genetic Code Table
codon_table = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': 'Stop', 'TAG': 'Stop',
    'TGC': 'C', 'TGT': 'C', 'TGA': 'Stop', 'TGG': 'W'
}


def translate_dna(dna_seq):
    """Translate a DNA sequence into a protein sequence."""
    protein_seq = []

    for i in range(0, len(dna_seq) - 2, 3):
        codon = dna_seq[i:i+3]
        amino_acid = codon_table.get(codon, "?")

        if amino_acid == "Stop":
            break

        protein_seq.append(amino_acid)

    return '-'.join(protein_seq)


# Step 1: Read DNA sequence from file
dna_sequence = read_dna_from_file("random_dna.txt")

# Step 2: Translate the sequence
protein_sequence = translate_dna(dna_sequence)

# Step 3: Print the result
print("DNA Sequence:", dna_sequence)
print("Protein Sequence:", protein_sequence)

# Step 4: Save to file
with open("protein_sequence.txt", "w") as file:
    file.write(protein_sequence)

print("Protein sequence saved to protein_sequence.txt")
