# Fetches FASTA from NCBI via Entrez URL (no Biopython needed), parses header from sequence, saves .fasta file, falls back to a built-in BRCA1 demo sequence if offline.
# Spent time learning about basics being used here using those + ai to help me build this project which consists of a lot of new stuff

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

