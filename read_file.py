def read_dna_from_file(filename):
    """Reads a DNA sequence from a file and removes whitespace/newlines."""
    with open(filename, "r") as file:
        return file.read().strip().replace("\n", "").upper()