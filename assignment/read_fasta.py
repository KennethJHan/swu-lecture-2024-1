import sys
from collections import defaultdict


def read_fasta(fasta_filepath: str) -> dict[str, int]:
    """Read DNA sequence from the file and return the count of each base.

    Args:
        fasta_filepath (str): File contains DNA sequence.

    Returns:
        dict[str, int]: Count of each base in the DNA sequence.

    Example:
        >>> read_fasta("NC_045512.fasta")
        {"A": 8954, "C": 5492, "G": 5863, "T": 9594}
    """
    data = defaultdict(int)
    with open(fasta_filepath) as handle:
        for line in handle:
            if line.startswith(">"):
                continue

            for base in line.strip():
                data[base] += 1

    return data


def make_result(data: dict[str, int]) -> str:
    """Make a string with the count of each base.

    Args:
        data (dict[str, int]): _description_

    Returns:
        str: Count of each base in the DNA sequence.

    Example:
        >>> make_result({"A": 8954, "C": 5492, "G": 5863, "T": 9594})
        "A: 8954\nC: 5492\nG: 5863\nT: 9594"
    """
    return f"A: {data['A']}\nC: {data['C']}\nG: {data['G']}\nT: {data['T']}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [sample.fasta]")
        sys.exit()

    data = read_fasta(sys.argv[1])
    print(make_result(data))
