codon_table = {
'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
'UUA': 'Leucine', 'UUG': 'Leucine', 'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}
def translate(rna_sequence):
#"""Converts RNA to protein sequence"""
    protein = []
    for i in range(0, len(rna_sequence)-2, 3):
        codon = rna_sequence[i:i+3]
        if codon_table.get(codon) == 'Stop':
            break
        protein.append(codon_table.get(codon, 'Unknown'))
    return '-'.join(protein)