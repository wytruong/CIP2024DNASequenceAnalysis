# DNA Sequence Analysis

This project is a DNA sequence analysis tool that calculates the GC content and identifies open reading frames (ORFs) in a given DNA sequence. The project consists of two main files: `main.py` and `dnasequence.py`.

## Features

- **GC Content Calculation**: Computes the percentage of guanine (G) and cytosine (C) in the DNA sequence.
- **ORF Identification**: Identifies open reading frames in the DNA sequence and translates them into proteins.

## Requirements

- Python 3.6+
- Biopython library

## Installation

1. **Clone the repository**:
   
   git clone https://github.com/yourusername/dna-sequence-analysis.git
   cd dna-sequence-analysis
   
3. **Install the required libraries**:
   
   pip install biopython

4. **Usage**:
   
   You can run the program either by entering a DNA sequence manually or by reading it from a file in FASTA format.

   **Manual Input**
   Run the program:
   
   python main.py
   Enter M when prompted to input the DNA sequence manually.
   Enter your DNA sequence when prompted.

   **File Input**
   Run the program:

   python main.py
   Enter F when prompted to read the DNA sequence from a file.
   Enter the file path to your FASTA file when prompted.

5. **Project Structure**

   dnasequence.py: Contains functions to calculate GC content, find ORFs, and validate the DNA sequence.
   main.py: The main script to run the DNA sequence analysis. It handles user input and displays results.

   Example Input:
   Enter 'M' for manual input or 'F' to read from file: M
   Enter the DNA sequence: ATGCGTAGCTAGCTGACTGATCGTAGCTAGCGTAGCTGACTG
   Example Output:
   
   Analysis Results:
   GC Content: 56.25%
   ORFs:
   - MVAS

6. **Author**
   My Truong
