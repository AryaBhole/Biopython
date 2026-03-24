# Computes sequence length, counts each nucleotide (A/T/G/C/N), calculates GC%, AT%, GC/AT ratio, and a sliding window GC profile (window=50, step=25).
#### Calculates GC/AT content, nucleotide frequencies, and sliding window GC.
# I know a lot about this file as something similar is used beafore in class

# These are now helper methods copied and modified from past pdf's and data

def count_nucleotides(sequence):
    counts = {"A": 0, "T": 0, "G": 0, "C": 0}
    for base in sequence:
        if base in counts:
            counts[base] += 1
        else :
            continue
    return counts

def nucleotide_frequency(sequence, counts=None):
    # If counts are not given, count the nucleotides first
    if counts is None:
        counts = count_nucleotides(sequence)
    total = len(sequence)
    # If sequence is empty, return 0 for all nucleotides
    if total == 0:
        result = {}
        for k in counts:
            result[k] = 0.0
        return result
    # Calculate percentage of each nucleotide
    result = {}
    for k, v in counts.items():
        percentage = (v / total) * 100
        result[k] = round(percentage, 4)
    return result

def calculate_gc_content(sequence):
    sequence = sequence.upper()
    g = sequence.count("G")
    c = sequence.count("C")
    return ((g + c) / len(sequence)) * 100 if len(sequence) > 0 else 0.0

def calculate_at_content(sequence):
    sequence = sequence.upper()
    a = sequence.count("A")
    t = sequence.count("T")
    return ((a + t) / len(sequence)) * 100 if len(sequence) > 0 else 0.0

# had to use ai for this one
def sliding_window_gc(sequence, window=50):
    sequence = sequence.upper()
    results  = []
    step     = max(1, window // 2)
    for i in range(0, len(sequence) - window + 1, step):
        win_seq = sequence[i:i + window]
        gc = calculate_gc_content(win_seq)
        results.append((i, gc))
    return results

# now this is the main analyzer which is using basic methods defined above it
def analyze_sequence(sequence):
    sequence = sequence.upper()
    print("\nStart Analyzer")

    counts = count_nucleotides(sequence)
    freq   = nucleotide_frequency(sequence, counts)
    gc     = calculate_gc_content(sequence)
    at     = calculate_at_content(sequence)
    ratio  = gc / at if at != 0 else 9999.0
    window = sliding_window_gc(sequence, window=50)

    results = {
        "length"            : len(sequence),
        "nucleotide_counts" : counts,
        "nucleotide_frequency": freq,
        "gc_content"        : gc,
        "at_content"        : at,
        "gc_at_ratio"       : ratio,
        "sliding_window_gc" : window,
    }

    print(f"  Length     : {results['length']} bp")
    print(f"  GC Content : {gc:.2f}%")
    print(f"  AT Content : {at:.2f}%")
    print(f"  GC/AT Ratio: {ratio:.4f}")
    print("End Analyzer\n")
    return results

# to print summary later in main file
def print_summary_table(analysis):
    #ai used to add this formatting as my code was really cluttered
    print("\n\n" + "=" * 50)
    print("     SEQUENCE ANALYSIS SUMMARY TABLE")
    print("=" * 50)
    print(f"  {'Sequence Length':<25} {analysis['length']:>10,} bp")
    print(f"  {'GC Content':<25} {analysis['gc_content']:>9.2f}%")
    print(f"  {'AT Content':<25} {analysis['at_content']:>9.2f}%")
    print(f"  {'GC/AT Ratio':<25} {analysis['gc_at_ratio']:>10.4f}")
    print("-" * 50)
    print(f"  {'Nucleotide':<15} {'Count':>10} {'Freq (%)':>10}")
    print("-" * 50)
    for nuc, count in analysis["nucleotide_counts"].items():
        freq = analysis["nucleotide_frequency"][nuc]
        print(f"  {nuc:<15} {count:>10,} {freq:>9.2f}%")
    print("=" * 50)