from unittest import mock
from unittest.mock import MagicMock, mock_open

from read_fasta import make_result, read_fasta


@mock.patch("builtins.open", new_callable=mock_open, read_data="AAGCTT")
def test_read_fasta(mock_open: MagicMock):
    data = read_fasta("NC_045512.fasta")
    assert data == {"A": 2, "G": 1, "C": 1, "T": 2}


def test_make_result():
    data = {"A": 8954, "C": 5492, "G": 5863, "T": 9594}
    assert make_result(data) == "A: 8954\nC: 5492\nG: 5863\nT: 9594"
