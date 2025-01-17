# CIP2024DNASequenceAnalysis

# DNA Sequence Analysis

This project is a DNA sequence analysis tool that calculates the GC content and identifies open reading frames (ORFs) in a given DNA sequence. The DNA Sequence Analysis Tool is a bioinformatics application designed to assist researchers and biologists in analyzing DNA sequences. This tool allows users to input any DNA sequence, including normal or mutated DNA. The program then calculates the GC content percentage and identifies existing Open Reading Frames (ORFs) within the given DNA sequence. By incorporating **NumPy**, the project efficiently processes large DNA datasets, ensuring better performance and memory usage. This project leverages Python's computational capabilities, including libraries like NumPy and Biopython, to provide accurate and efficient DNA sequence analysis.

The project consists of two main files: `main.py` and `dnasequence.py`.

## Features

- **GC Content Calculation**: Computes the percentage of guanine (G) and cytosine (C) in the DNA sequence. The GC content is calculated using **NumPy arrays** for efficient element-wise operations. The formula used is:
  \[
  \text{GC Content (\%)} = \left(\frac{\text{Number of Gs and Cs}}{\text{Total number of bases}}\right) \times 100
  \]

- **ORF Identification**: Identifies open reading frames in the DNA sequence and translates them into proteins. ORFs are sequences of DNA that have the potential to code for proteins. The tool uses **NumPy arrays** for faster slicing and filtering to identify start codons (e.g., "ATG") and stop codons ("TAA," "TAG," "TGA").

- **Validation Using NumPy**: DNA sequence validation ensures that the input contains only valid characters (`A`, `T`, `C`, `G`). This process uses NumPy's array comparison for efficient validation.

## Requirements

- Python 3.6+
- Biopython library
- NumPy library

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/wytruong/CIP2024DNASequenceAnalysis.git
   cd CIP2024DNASequenceAnalysis
2. **Install the required libraries**:
   ```sh
   pip install biopython numpy

## Usage
You can run the program either by entering a DNA sequence manually or by reading it from a file in FASTA format.

**Manual Input**:
1. Run the program: python main.py
2. Enter M when prompted to input the DNA sequence manually.
3. Enter your DNA sequence when prompted.
   
**File Input**:
1. Run the program: python main.py
2. Enter F when prompted to read the DNA sequence from a file.
3. Enter the file path to your FASTA file when prompted.

## Project Structure

- **dnasequence.py**: Contains functions to calculate GC content, find ORFs, and validate the DNA sequence using NumPy arrays for efficient processing.
- **main.py**: The main script to run the DNA sequence analysis. It handles user input, integrates dnasequence.py functionality, and displays results.

## Benefit of Using NummPy
- **Efficient Memory Usage**: NumPy arrays use less memory compared to Python lists, especially when working with large DNA datasets.
- **Faster Computation**: Operations like element-wise comparisons and slicing are optimized in NumPy, making GC content calculation and ORF identification faster.
- **Scalability**: The program can now handle large DNA sequences (e.g., genomic data) with improved performance.

## Author
My Truong - github.com/wytruong


   
