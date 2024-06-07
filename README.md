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
   
   git clone https://github.com/wytruong/CIP2024DNASequenceAnalysis.git<br>
   cd CIP2024DNASequenceAnalysis
   
3. **Install the required libraries**:
   
   pip install biopython

4. **Usage**:
   
   You can run the program either by entering a DNA sequence manually or by reading it from a file in FASTA format.

   **Manual Input**
   Run the program:<br><br>
   
   python main.py<br>
   Enter M when prompted to input the DNA sequence manually.<br>
   Enter your DNA sequence when prompted.<br>

   **File Input**
   Run the program:<br><br>

   python main.py<br>
   Enter F when prompted to read the DNA sequence from a file.<br>
   Enter the file path to your FASTA file when prompted.<br>

5. **Project Structure**

   dnasequence.py: Contains functions to calculate GC content, find ORFs, and validate the DNA sequence.<br>
   main.py: The main script to run the DNA sequence analysis. It handles user input and displays results.<br>

   Example Input:<br>
   Enter 'M' for manual input or 'F' to read from file: M<br>
   Enter the DNA sequence: ATGCGTAGCTAGCTGACTGATCGTAGCTAGCGTAGCTGACTG<br>
   Example Output:<br><br>
   
   Analysis Results:<br>
   GC Content: 56.25%<br>
   ORFs:<br>
   - MVAS<br>

6. **Author**<br>
   My Truong
