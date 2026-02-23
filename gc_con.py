def calculate_gc_content(dna_seq):
    """Calculates the GC content percentage in a DNA sequence."""
    if len(dna_seq) == 0:
        return 0  # Avoid division by zero

    gc_count = dna_seq.count('G') + dna_seq.count('C')
    gc_percentage = (gc_count / len(dna_seq)) * 100

    return round(gc_percentage, 2)
