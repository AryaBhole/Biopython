# from Bio.Seq import Seq
# out = Seq("ATGAGTCGATGCTTAGGTCGGCTAGCTTAG")
# print (out.translate())

from Bio import SeqIO
from Bio.Seq import Seq
# Read the FASTA file
with open("fasta_dna.txt", "r") as fasta_file:
    for record in SeqIO.parse(fasta_file, "fasta"):
        dna_seq = record.seq # Extract the sequence
        protein_seq = dna_seq.translate() # Translate to protein
        print(f"Original DNA: {dna_seq}")
        print(f"Translated Protein: {protein_seq}")