from Bio.Seq import Seq

def calculate_gc_content(seq):
    """Calculate GC content of a DNA sequence."""
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100

def find_orfs(seq):
    """Find all open reading frames (ORFs) in a DNA sequence."""
    orfs = []
    seq_length = len(seq)
    for frame in range(3):
        for i in range(frame, seq_length, 3):
            codon = seq[i:i+3]
            if codon == "ATG":
                protein = seq[i:].translate(to_stop=True)
                orfs.append(protein)
                break  # Only consider the first ORF in this frame for simplicity
    return orfs

def analyze_dna_sequence(seq):
    """Perform analysis on the given DNA sequence."""
    seq_obj = Seq(seq)
    results = {
        'GC Content': calculate_gc_content(seq_obj),
        'ORFs': find_orfs(seq_obj)
    }
    return results

def is_valid_dna_sequence(seq):
    """Check if a DNA sequence contains only valid characters (A, T, C, G)."""
    valid_bases = {'A', 'T', 'C', 'G'}
    return all(base in valid_bases for base in seq)