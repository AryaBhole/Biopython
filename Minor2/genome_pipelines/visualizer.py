# Generates 6 publication-quality plots — nucleotide frequency bar chart, GC/AT pie charts, codon usage heatmap, sliding window GC line plot, ORF length bar chart by frame, and motif occurrence summary.

# learned about heatmap so sns is required
#### Generates 6 plots: nucleotide bar, GC/AT pie, codon heatmap, sliding-window GC, ORF lengths, and motif summary

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#output_path = r"C:\Users\bhole\OneDrive\Desktop\Arya\Python\Biopython\Biopython\Minor2\genome_pipelines\pipeline_output"

# Bar plot of nucleotide frequency
def plot_nucleotide_frequency(analysis, output_path):
    freq = analysis["nucleotide_frequency"]
    labels = list(freq.keys())
    values = list(freq.values())
    plt.figure()
    plt.bar(labels, values)
    plt.title("Nucleotide Frequency")
    plt.xlabel("Nucleotide")
    plt.ylabel("Percentage")
    plt.savefig(output_path)
    plt.close()
    print("Saved:", output_path)

# Pie chart for GC vs AT
def plot_gc_at_pie(analysis, output_path):
    gc = analysis["gc_content"]
    at = analysis["at_content"]
    plt.figure()
    plt.pie([gc, at],
            labels=["GC", "AT"],
            autopct="%1.1f%%")
    plt.title("GC vs AT Content")
    plt.savefig(output_path)
    plt.close()
    print("Saved:", output_path)

# Codon heatmap
def plot_codon_heatmap(codon_counts, output_path):
    codons = list(codon_counts.keys())
    counts = list(codon_counts.values())
    data = np.array(counts).reshape(-1,1)
    plt.figure()
    sns.heatmap(data,
                yticklabels=codons,
                xticklabels=["Count"])
    plt.title("Codon Usage Heatmap")
    plt.savefig(output_path)
    plt.close()
    print("Saved:", output_path)

# GC sliding window plot
def plot_gc_window(window_gc, output_path):
    positions = [x[0] for x in window_gc]
    gc_vals = [x[1] for x in window_gc]
    plt.figure()
    plt.plot(positions, gc_vals)
    plt.title("GC Content Across Sequence")
    plt.xlabel("Position")
    plt.ylabel("GC %")
    plt.savefig(output_path)
    plt.close()
    print("Saved:", output_path)

# ORF length bar plot
def plot_orf_lengths(orfs, output_path):
    lengths = [o["length"] for o in orfs]
    plt.figure()
    plt.bar(range(len(lengths)), lengths)
    plt.title("ORF Lengths")
    plt.xlabel("ORF number")
    plt.ylabel("Length")
    plt.savefig(output_path)
    plt.close()
    print("Saved:", output_path)

# Motif summary plot
def plot_motif_summary(motif_results, output_path):
    names = list(motif_results.keys())
    counts = [len(v) for v in motif_results.values()]
    plt.figure()
    plt.bar(names, counts)
    plt.title("Motif Occurrences")
    plt.xlabel("Motif")
    plt.ylabel("Count")
    plt.savefig(output_path)
    plt.close()
    print("Saved:", output_path)

def generate_all_plots(analysis, orfs, motifs, codon_counts, prefix=output_path + "/"):
    plot_nucleotide_frequency(analysis, prefix + "nucleotide_freq.png")
    plot_gc_at_pie(analysis, prefix + "gc_at_pie.png")
    plot_codon_heatmap(codon_counts, prefix + "codon_heatmap.png")
    plot_gc_window(analysis["sliding_window_gc"],
                   prefix + "gc_window.png")
    plot_orf_lengths(orfs, prefix + "orf_lengths.png")
    plot_motif_summary(motifs, prefix + "motif_summary.png")
    print("All plots created")