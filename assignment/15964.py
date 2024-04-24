import pytest


def p_15964(A: int, B: int) -> int:
    """

    Args:
        A (int): input number A.
        B (int): input number B.

    Returns:
        int: The result of (A+B)×(A-B).

    Examples:
        >>> p_15964(4, 3)
        7
        >>> p_15964(3, 4)
        -7
    """
    return (A + B) * (A - B)


@pytest.mark.parametrize(
    "A, B, expected",
    [
        (4, 3, 7),
        (3, 4, -7),
    ],
)
def test_p_15964(A, B, expected):
    assert p_15964(A, B) == expected


if __name__ == "__main__":
    A, B = map(int, input().split())
    print(p_15964(A, B))
