# main.py
# Runs the genome analysis pipeline using different modules

from sequence_fetcher import fetch_sequence_from_ncbi, save_fasta
from sequence_analyzer import analyze_sequence, print_summary_table
from orf_motif_finder import find_orfs, find_motifs, print_orf_table, codon_usage
from visualizer import generate_all_plots
import os

# This ACCESSION can be changed to any valid id to get the particular plots
ACCESSION  = "NM_000546"
DB         = "nucleotide"
MIN_ORF    = 90
OUTPUT_DIR = "pipeline_output"

def main():
    # Fetch sequence from NCBI sequence fetcher file
    seq_data = fetch_sequence_from_ncbi(ACCESSION, DB)
    sequence = seq_data["sequence"]

    # Save FASTA file
    fasta_file = os.path.join(OUTPUT_DIR, f"{ACCESSION}.fasta")
    save_fasta(seq_data, fasta_file)

    # Analyzer file
    analysis = analyze_sequence(sequence)
    print_summary_table(analysis)

    # ORF file
    orfs = find_orfs(sequence, MIN_ORF)
    print_orf_table(orfs)

    motifs = find_motifs(sequence)
    codon_counts = codon_usage(sequence)
    
    # Visualizer file
    generate_all_plots(analysis, orfs, motifs, codon_counts, OUTPUT_DIR + "/")
    print("\nPipeline finished successfully\n")

if __name__ == "__main__":
    main()