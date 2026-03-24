# Computes sequence length, counts each nucleotide (A/T/G/C/N), calculates GC%, AT%, GC/AT ratio, and a sliding window GC profile (window=50, step=25).
#### Calculates GC/AT content, nucleotide frequencies, and sliding window GC.
# I know a lot about this file as something similar is used before in class

# These are helper methods copied and modified from past pdf's and data

def count_nucleotides(sequence):
    counts = {"A":0, "T":0, "G":0, "C":0}
    for base in sequence.upper():
        if base in counts:
            counts[base] += 1
    return counts


def nucleotide_frequency(sequence, counts=None):
    # If counts are not given, count nucleotides first
    if counts is None:
        counts = count_nucleotides(sequence)

    total = len(sequence)

    # If sequence empty return 0
    if total == 0:
        return {k:0.0 for k in counts}

    result = {}
    for k in counts:
        result[k] = round((counts[k] / total) * 100, 4)

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


# sliding window GC
def sliding_window_gc(sequence, window=50):
    sequence = sequence.upper()
    results = []
    step = window // 2

    for i in range(0, len(sequence) - window + 1, step):
        part = sequence[i:i+window]
        gc = calculate_gc_content(part)
        results.append((i, gc))

    return results


# main analyzer which uses methods above
def analyze_sequence(sequence):
    sequence = sequence.upper()
    print("\nStart Analyzer")

    counts = count_nucleotides(sequence)
    freq = nucleotide_frequency(sequence, counts)
    gc = calculate_gc_content(sequence)
    at = calculate_at_content(sequence)

    ratio = gc / at if at != 0 else 0
    window = sliding_window_gc(sequence, 50)

    results = {
        "length": len(sequence),
        "nucleotide_counts": counts,
        "nucleotide_frequency": freq,
        "gc_content": gc,
        "at_content": at,
        "gc_at_ratio": ratio,
        "sliding_window_gc": window,
    }

    print("Length:", results["length"], "bp")
    print("GC Content:", round(gc,2), "%")
    print("AT Content:", round(at,2), "%")
    print("GC/AT Ratio:", round(ratio,2))
    print("End Analyzer\n")

    return results


# to print summary later in main file
def print_summary_table(analysis):
    print("\nSequence Analysis Summary")

    print("Sequence Length:", analysis["length"], "bp")
    print("GC Content:", round(analysis["gc_content"],2), "%")
    print("AT Content:", round(analysis["at_content"],2), "%")
    print("GC/AT Ratio:", round(analysis["gc_at_ratio"],4))

    print("\nNucleotide Counts and Frequency")

    for nuc in analysis["nucleotide_counts"]:
        count = analysis["nucleotide_counts"][nuc]
        freq = analysis["nucleotide_frequency"][nuc]
        print(nuc, "Count:", count, "Frequency:", round(freq,2), "%")