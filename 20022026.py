from bioinformatics_tools import complement, gc_content, transcribe, translate
# Example DNA sequence
dna_seq = "ATGCCGCGTACACGGCAGCAGAACGTACGCTAACGC"
# DNA Operations
print("DNA Complement:", complement(dna_seq))
print("GC Content:", gc_content(dna_seq), "%")
# RNA Transcription
rna_seq = transcribe(dna_seq)
print("RNA Transcription:", rna_seq)
# Protein Translation
protein_seq = translate(rna_seq)
print("Protein Translation:", protein_seq)