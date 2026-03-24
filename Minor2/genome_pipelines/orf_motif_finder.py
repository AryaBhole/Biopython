# An Open Reading Frame (ORF) is a continuous stretch of codons that begins with a start codon (ATG) and ends with a stop codon (TAA, TAG, TGA).
# Scans all 6 reading frames (+1,+2,+3 and reverse complement -1,-2,-3) for ORFs between ATG and stop codons (TAA/TAG/TGA), translates ORFs using the standard genetic code, and searches for 8 known biological motifs (TATA box, Kozak, Shine-Dalgarno, CpG islands, splice sites, etc.) using regex.

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

# known motifs which i had to look up for this through ai
KNOWN_MOTIFS = {
    "TATA_box"       : r"TATA[AT]A[AT]",
    "Kozak_sequence" : r"[AG]CCATGG",
    "Splice_donor"   : r"GT[AG]AGT",
    "CpG_island"     : r"CG",
    "Shine_Dalgarno" : r"AGGAGG",
    "CAAT_box"       : r"GGCCAATCT",
    "GC_box"         : r"GGGCGG",
}

# known earlier
def reverse_complement(sequence):
    complement = {"A":"T","T":"A","G":"C","C":"G","N":"N"}
    return "".join(complement.get(b, "N") for b in reversed(sequence.upper()))

def translate_sequence(dna_seq):
    protein = []
    for i in range(0, len(dna_seq) - 2, 3):
        codon = dna_seq[i:i+3].upper()
        aa    = CODON_TABLE.get(codon, "?")
        if aa == "*":
            protein.append("*")
            break
        protein.append(aa)
    return "".join(protein)

def find_motifs(sequence, custom_motifs=None):
    sequence   = sequence.upper()
    all_motifs = dict(KNOWN_MOTIFS)
    if custom_motifs:
        all_motifs.update(custom_motifs)
    print(f"\n[Motif Finder] Scanning for {len(all_motifs)} motif types...")
    results = {}
    for name, pattern in all_motifs.items():
        matches = [{"start":m.start(),"end":m.end(),"matched":m.group()}
                   for m in re.finditer(pattern, sequence)]
        results[name] = matches
        status = f"{len(matches)} hit(s) (first at {matches[0]['start']})" if matches else "0 hits"
        print(f"  {name:<22}: {status}")
    return results

def codon_usage(sequence):
    sequence = sequence.upper()
    usage    = defaultdict(int)
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if len(codon) == 3:
            usage[codon] += 1
    return dict(sorted(usage.items()))

# used ai to build this as orf was not known to me beafore
def find_orfs(sequence, min_length=100):
    sequence = sequence.upper()
    print(f"[ORF Finder] Scanning 6 frames (min length={min_length} bp)...")
    all_orfs = []
    for frame in range(3):
        all_orfs.extend(_scan_frame(sequence, frame, "+"))
    rev_comp = reverse_complement(sequence)
    for frame in range(3):
        all_orfs.extend(_scan_frame(rev_comp, frame, "-", len(sequence)))
    filtered = [o for o in all_orfs if o["length"] >= min_length]
    filtered.sort(key=lambda x: x["length"], reverse=True)
    print(f"[ORF Finder] Total: {len(all_orfs)} | Filtered: {len(filtered)}")
    return filtered

def _scan_frame(sequence, frame_offset, strand, original_len=None):
    orfs = []
    in_orf = False
    orf_start = 0
    frame_label = ("+" if strand == "+" else "-") + str(frame_offset + 1)
    i = frame_offset
    while i < len(sequence) - 2:
        codon = sequence[i:i+3]
        if len(codon) < 3:
            break
        if not in_orf and codon == START_CODON:
            in_orf    = True
            orf_start = i
        elif in_orf and codon in STOP_CODONS:
            orf_seq = sequence[orf_start:i+3]
            protein = translate_sequence(orf_seq)
            if strand == "-" and original_len:
                real_start = original_len - (i + 3)
                real_end   = original_len - orf_start
            else:
                real_start = orf_start
                real_end   = i + 3
            orfs.append({"frame":frame_label,"start":real_start,
                         "end":real_end,"length":len(orf_seq),
                         "orf_seq":orf_seq,"protein":protein})
            in_orf = False
        i += 3
    return orfs

# this is for later
def print_orf_table(orfs, top_n=10):
    print("\n" + "=" * 70)
    print(f"  TOP {min(top_n, len(orfs))} ORFs (sorted by length)")
    print("=" * 70)
    print(f"  {'#':<4} {'Frame':<8} {'Start':>8} {'End':>8} {'Length':>8}  Protein preview")
    print("-" * 70)
    for idx, orf in enumerate(orfs[:top_n]):
        preview = orf["protein"][:20] + ("..." if len(orf["protein"]) > 20 else "")
        print(f"  {idx+1:<4} {orf['frame']:<8} {orf['start']:>8,} "
              f"{orf['end']:>8,} {orf['length']:>7,}  {preview}")
    print("=" * 70)