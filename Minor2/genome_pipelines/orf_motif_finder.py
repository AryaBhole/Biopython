# orf_motif_finder.py
# An Open Reading Frame (ORF) is a continuous stretch of codons that begins with a start codon (ATG)
# and ends with a stop codon (TAA, TAG, TGA).
# Scans all 6 reading frames (+1,+2,+3 and reverse complement -1,-2,-3)

#### Detects ORFs in all 6 reading frames and searches for sequence motifs.

import re
from collections import defaultdict

# codon table and their nature is known so using it
START_CODON = "ATG"
STOP_CODONS = {"TAA", "TAG", "TGA"}

CODON_TABLE = {
    "TTT":"F","TTC":"F","TTA":"L","TTG":"L","CTT":"L","CTC":"L","CTA":"L","CTG":"L",
    "ATT":"I","ATC":"I","ATA":"I","ATG":"M","GTT":"V","GTC":"V","GTA":"V","GTG":"V",
    "TCT":"S","TCC":"S","TCA":"S","TCG":"S","CCT":"P","CCC":"P","CCA":"P","CCG":"P",
    "ACT":"T","ACC":"T","ACA":"T","ACG":"T","GCT":"A","GCC":"A","GCA":"A","GCG":"A",
    "TAT":"Y","TAC":"Y","TAA":"*","TAG":"*","CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "AAT":"N","AAC":"N","AAA":"K","AAG":"K","GAT":"D","GAC":"D","GAA":"E","GAG":"E",
    "TGT":"C","TGC":"C","TGA":"*","TGG":"W","CGT":"R","CGC":"R","CGA":"R","CGG":"R",
    "AGT":"S","AGC":"S","AGA":"R","AGG":"R","GGT":"G","GGC":"G","GGA":"G","GGG":"G",
}

# known motifs which i had to look up for this through web
KNOWN_MOTIFS = {
    "TATA_box" : r"TATA[AT]A[AT]",
    "Kozak_sequence" : r"[AG]CCATGG",
    "Splice_donor" : r"GT[AG]AGT",
    "CpG_island" : r"CG",
    "Shine_Dalgarno" : r"AGGAGG",
    "CAAT_box" : r"GGCCAATCT",
    "GC_box" : r"GGGCGG",
}

# known earlier
def reverse_complement(sequence):
    complement = {"A":"T","T":"A","G":"C","C":"G","N":"N"}
    seq = sequence.upper()
    return "".join(complement.get(b,"N") for b in reversed(seq))

def translate_sequence(dna_seq):
    protein = []
    for i in range(0, len(dna_seq)-2, 3):
        codon = dna_seq[i:i+3].upper()
        aa = CODON_TABLE.get(codon, "?")
        if aa == "*":      # stop codon
            break
        protein.append(aa)

    return "".join(protein)

def find_motifs(sequence, custom_motifs=None):
    sequence = sequence.upper()
    motifs = KNOWN_MOTIFS.copy()
    if custom_motifs:
        motifs.update(custom_motifs)

    print("\n[Motif Finder] Searching motifs...")

    results = {}

    for name, pattern in motifs.items():
        matches = []
        for m in re.finditer(pattern, sequence):
            matches.append({
                "start": m.start(),
                "end": m.end(),
                "matched": m.group()
            })

        results[name] = matches
        print(name, ":", len(matches), "hits")

    return results

def codon_usage(sequence):
    sequence = sequence.upper()
    usage = defaultdict(int)

    for i in range(0, len(sequence)-2, 3):
        codon = sequence[i:i+3]
        if len(codon) == 3:
            usage[codon] += 1

    return dict(usage)

# used ai to build this as orf was not known to me before
def find_orfs(sequence, min_length=100):
    sequence = sequence.upper()
    print("[ORF Finder] Scanning frames...")
    all_orfs = []

    # forward frames
    for frame in range(3):
        all_orfs.extend(_scan_frame(sequence, frame, "+"))

    # reverse frames
    rev = reverse_complement(sequence)

    for frame in range(3):
        all_orfs.extend(_scan_frame(rev, frame, "-"))

    # filter by length
    filtered = []

    for o in all_orfs:
        if o["length"] >= min_length:
            filtered.append(o)

    filtered.sort(key=lambda x: x["length"], reverse=True)
    print("Total ORFs:", len(all_orfs))
    print("Filtered ORFs:", len(filtered))
    return filtered

def _scan_frame(sequence, frame_offset, strand):
    orfs = []
    in_orf = False
    start = 0
    frame_label = strand + str(frame_offset + 1)
    i = frame_offset

    while i < len(sequence)-2:
        codon = sequence[i:i+3]
        if not in_orf and codon == START_CODON:
            in_orf = True
            start = i

        elif in_orf and codon in STOP_CODONS:

            orf_seq = sequence[start:i+3]

            protein = translate_sequence(orf_seq)

            orfs.append({
                "frame": frame_label,
                "start": start,
                "end": i+3,
                "length": len(orf_seq),
                "orf_seq": orf_seq,
                "protein": protein
            })

            in_orf = False

        i += 3

    return orfs

# this is for later
def print_orf_table(orfs, top_n=5):
    print("\nTop ORFs")
    print(f"{'#':<4}{'Frame':<6}{'Start':<8}{'End':<8}{'Length':<8}{'Protein Preview'}")

    for i, orf in enumerate(orfs[:top_n], 1):
        preview = orf["protein"][:20]

        print(
            f"{i:<4}"
            f"{orf['frame']:<6}"
            f"{orf['start']:<8}"
            f"{orf['end']:<8}"
            f"{orf['length']:<8}"
            f"{preview}"
        )