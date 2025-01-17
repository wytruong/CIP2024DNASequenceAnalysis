from dnasequence import analyze_dna_sequence, is_valid_dna_sequence
from Bio import SeqIO

def read_sequence_from_file(file_path):
    """Read a sequence from a file in FASTA format."""
    with open(file_path, "r") as file:
        record = SeqIO.read(file, "fasta")
    return str(record.seq)

def main():
    while True:
        choice = input("Enter 'M' for manual input or 'F' to read from file: ").strip().upper()

        if choice == 'M':
            seq_input = input("Enter the DNA sequence: ").strip().upper()
            if not is_valid_dna_sequence(seq_input):
                print("Invalid DNA sequence. Please enter a sequence containing only A, T, C, G.")
                continue
            results = analyze_dna_sequence(seq_input)
            break

        elif choice == 'F':
            file_path = input("Enter the file path: ").strip()
            try:
                seq_input = read_sequence_from_file(file_path).upper()
                if not is_valid_dna_sequence(seq_input):
                    print("Invalid DNA sequence in file. Please provide a valid file.")
                    continue
                results = analyze_dna_sequence(seq_input)
                break
            except FileNotFoundError:
                print("File not found. Please check the path and try again.")
            except Exception as e:
                print(f"An error occurred while reading the file: {e}")
                continue

        else:
            print("Invalid choice. Please enter 'M' or 'F'.")
            continue

    print("\nAnalysis Results:")
    for key, value in results.items():
        print(f"{key}: {value}")
        if isinstance(value, list):
            for item in value:
                print(f" - {item}")

if __name__ == "__main__":
    main()
