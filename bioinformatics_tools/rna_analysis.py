def transcribe(dna_sequence):
#"""Converts a DNA sequence to RNA (T -> U)"""
    return dna_sequence.replace('T', 'U')

def reverse_transcribe(rna_sequence):
#"""Converts an RNA sequence back to DNA (U -> T)"""
    return rna_sequence.replace('U', 'T')