# main.py
# Runs the genome analysis pipeline using different modules

# Don't know about acssion id stuff so had to use ai again

from sequence_fetcher import fetch_sequence_from_ncbi, save_fasta
from sequence_analyzer import analyze_sequence, print_summary_table
from orf_motif_finder import find_orfs, find_motifs, print_orf_table
from visualizer import generate_all_plots
import os

# Default parameters (given in assignment)
ACCESSION  = "NM_007294"      # BRCA1 mRNA
DB         = "nucleotide"
MIN_ORF    = 90
OUTPUT_DIR = "pipeline_output"

def main():

    print("\n=== GENOME ANALYSIS PIPELINE ===\n")
    # Create output folder if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 1️⃣ Fetch sequence from NCBI
    seq_data = fetch_sequence_from_ncbi(ACCESSION, DB)
    sequence = seq_data["sequence"]

    # 2️⃣ Save FASTA file
    fasta_file = os.path.join(OUTPUT_DIR, f"{ACCESSION}.fasta")
    save_fasta(seq_data, fasta_file)

    # 3️⃣ Analyze sequence
    analysis = analyze_sequence(sequence)

    # Print results
    print_summary_table(analysis)

    # 4️⃣ Detect ORFs
    orfs = find_orfs(sequence, MIN_ORF)

    print_orf_table(orfs)

    # 5️⃣ Find motifs
    motifs = find_motifs(sequence)

    # 6️⃣ Visualize results
    generate_all_plots(analysis, orfs, motifs, OUTPUT_DIR)
    print("\nPipeline finished successfully\n")

if __name__ == "__main__":
    main()