import numpy as np
from Bio.Seq import Seq

def calculate_gc_content(seq):
    """Calculate GC content of a DNA sequence using NumPy."""
    seq_array = np.array(list(seq))  # Convert sequence into a NumPy array
    gc_count = np.sum((seq_array == 'G') | (seq_array == 'C'))  # Count G and C
    return (gc_count / len(seq_array)) * 100

def find_orfs(seq):
    """Find all open reading frames (ORFs) in a DNA sequence using NumPy."""
    seq_array = np.array(list(seq))  # Convert sequence into a NumPy array
    seq_length = len(seq_array)
    orfs = []

    for frame in range(3):
        codons = np.array(["".join(seq_array[i:i+3]) for i in range(frame, seq_length - 2, 3)])
        start_indices = np.where(codons == "ATG")[0]  # Find indices of start codons
        for start in start_indices:
            protein = Seq(seq[start * 3:]).translate(to_stop=True)  # Translate to protein
            orfs.append(protein)
            break  # Only consider the first ORF in this frame for simplicity

    return orfs

def is_valid_dna_sequence(seq):
    """Check if a DNA sequence contains only valid characters (A, T, C, G) using NumPy."""
    valid_bases = np.array(['A', 'T', 'C', 'G'])
    seq_array = np.array(list(seq))
    return np.isin(seq_array, valid_bases).all()

def analyze_dna_sequence(seq):
    """Perform analysis on the given DNA sequence."""
    gc_content = calculate_gc_content(seq)
    orfs = find_orfs(seq)
    return {
        'GC Content': gc_content,
        'ORFs': orfs
    }
