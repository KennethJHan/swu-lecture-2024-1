import sys
from collections import defaultdict


def read_dna(filepath: str) -> dict[str, int]:
    """Read DNA sequence from the file and return the count of each base.

    Args:
        filepath (str): File contains DNA sequence.

    Returns:
        dict[str, int]: Count of each base in the DNA sequence.

    Example:
        >>> read_dna("DNA.txt")
        {"A": 20, "G": 17, "C": 12, "T": 21}
    """
    data = defaultdict(int)
    seq = str()
    with open(filepath) as handle:
        for line in handle:
            seq += line.strip()

    for base in seq:
        data[base] += 1

    return data


def make_result(data: dict[str, int]) -> str:
    """Make a string with the count of each base.

    Args:
        data (dict[str, int]): Count of each base in the DNA sequence.

    Returns:
        str: Space-separated count of each base.

    Example:
        >>> make_result({"A": 20, "G": 17, "C": 12, "T": 21})
        "20 12 17 21"
    """
    return f"{data['A']} {data['C']} {data['G']} {data['T']}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [DNA.txt]")
        sys.exit()

    data = read_dna(sys.argv[1])
    print(make_result(data))
