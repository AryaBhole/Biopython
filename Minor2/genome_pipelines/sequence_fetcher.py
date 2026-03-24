# Fetches FASTA from NCBI via Entrez URL (no Biopython needed), parses header from sequence, saves .fasta file, falls back to a built-in BRCA1 demo sequence if offline.
# Spent time learning about basics being used here using those + ai to help me build this project which consists of a lot of new stuff

#### Fetches DNA sequences from NCBI or uses a demo sequence.

# had to look this up
import urllib.request
NCBI_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# for fall back we cound use a error catch to just simply return process failed but this is better
def _demo_sequence():
    demo_seq = (
        "ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAAT"
        "CTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACAT"
        "TCAACTCAGGAGTCAAGAATTTGAAGTCAGCACAAGTAAATGTCAGTTGTCTCCAGATGAGCA"
        "GTCTGCACTTGTACAAGAAGCTGAAGAAAATGAAGAAAAGATTTCAAATGATTTCAGAAGAAG"
        "TTGTAAAGCAAATTTGTACAGAAATTGAAGCCAGTCATTATGAAGAAATGTCTCCAGAAGCTG"
        "AGGAAATGGAGAAAGCAGAAGAAGAAAGAAAAAAGAAAGAGCTTCAAGAGAAACGAAAGAAAGA"
        "GCAAGAGAAAGAGAAAGAGAAACAGAAGGAACGGAAAGAGAAAGAGCTTCAAGAAAAGGAAAGA"
        "ACAGAAGGAAGAGAAAGAGCTTCAAGAGAAACAGAAGAAAGAGCAAGAGAAAGAGAAAGAGAAA"
    )
    print("[Fetcher] Using DEMO: BRCA1 partial sequence (506 bp)")
    return {
        "accession"  : "DEMO_BRCA1",
        "description": "Demo BRCA1 partial sequence (synthetic)",
        "sequence"   : demo_seq,
        "seq_type"   : "DNA"
    }

# New stuff i had to use ai and other tools and learning to put here

def fetch_sequence_from_ncbi(accession_id, db="nucleotide"):
    print(f"[Fetcher] Connecting to NCBI for: {accession_id}")
    url = (f"{NCBI_EFETCH}?db={db}&id={accession_id}"
           f"&rettype=fasta&retmode=text&email=student@example.com")
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            fasta_text = resp.read().decode("utf-8")
        return _parse_fasta(fasta_text, accession_id)
    
    # the fallback mechanism disscussed beafore
    except Exception as e:
        print(f"[Fetcher] Could not connect: {e}")
        print("[Fetcher] Using built-in demo sequence.")
        return _demo_sequence()

def _parse_fasta(fasta_text, accession_id):
    lines = fasta_text.strip().splitlines()
    if not lines or not lines[0].startswith(">"):
        return _demo_sequence()
    header   = lines[0][1:]
    sequence = "".join(lines[1:]).upper()
    is_dna   = all(c in "ACGTN" for c in sequence[:100])
    print(f"[Fetcher] Got: {header[:60]}")
    print(f"[Fetcher] Length: {len(sequence)} bp")
    return {
        "accession"  : accession_id,
        "description": header,
        "sequence"   : sequence,
        "seq_type"   : "DNA" if is_dna else "Protein"
    }

#filepath = r"C:\Users\bhole\OneDrive\Desktop\Arya\Python\Biopython\Biopython\Minor2\genome_pipelines\pipeline_output"

def save_fasta(seq_data, filepath):
    with open(filepath, "w") as f:
        f.write(f">{seq_data['accession']} {seq_data['description']}\n")
        seq = seq_data["sequence"]
        for i in range(0, len(seq), 60):
            f.write(seq[i:i+60] + "\n")
    print(f"[Fetcher] FASTA saved to: {filepath}")