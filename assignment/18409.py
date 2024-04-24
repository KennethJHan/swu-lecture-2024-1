import pytest


def p_18409(string: str) -> int:
    """Count the number of vowels in given string.

    Args:
        string (str): The string to count the number of vowels.

    Returns:
        int: The number of vowels in given string.

    Examples:
        >>> p_18409("joiyosen")
        4
        >>> p_18409("bitaro")
        3
    """
    result = 0
    vowel = {"a", "i", "u", "e", "o"}
    for char in string:
        if char in vowel:
            result += 1

    return result


@pytest.mark.parametrize(
    "string, expected",
    [
        ("joiyosen", 4),
        ("bitaro", 3),
    ],
)
def test_p_18409(string: str, expected: int):
    assert p_18409(string) == expected


if __name__ == "__main__":
    _ = input()
    string = input()
    print(p_18409(string))
