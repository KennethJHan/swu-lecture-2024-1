from unittest import mock
from unittest.mock import MagicMock, mock_open

from DNA import make_result, read_dna


@mock.patch("builtins.open", new_callable=mock_open, read_data="AAGCTT")
def test_read_dna(mock_open: MagicMock):
    data = read_dna("DNA.txt")
    assert data == {"A": 2, "G": 1, "C": 1, "T": 2}


def test_make_result():
    data = {"A": 20, "G": 17, "C": 12, "T": 21}
    assert make_result(data) == "20 12 17 21"
