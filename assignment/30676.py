import pytest


def p_30676(frequency: int) -> str:
    """Return color of given frequency.

    Notes:
        빨간색: 620nm 이상 780nm 이하
        주황색: 590nm 이상 620nm 미만
        노란색: 570nm 이상 590nm 미만
        초록색: 495nm 이상 570nm 미만
        파란색: 450nm 이상 495nm 미만
        남색: 425nm 이상 450nm 미만
        보라색: 380nm 이상 425nm 미만

    Args:
        frequency (int): The frequency of light.

    Returns:
        str: The color of given frequency.

    Examples:
        >>> p_30676(627)
        Red
        >>> p_30676(516)
        Green
    """
    if 620 <= frequency <= 780:
        return "Red"
    elif 590 <= frequency < 620:
        return "Orange"
    elif 570 <= frequency < 590:
        return "Yellow"
    elif 495 <= frequency < 570:
        return "Green"
    elif 450 <= frequency < 495:
        return "Blue"
    elif 425 <= frequency < 450:
        return "Indigo"
    elif 380 <= frequency < 425:
        return "Violet"


@pytest.mark.parametrize(
    "frequency, expected",
    [
        (627, "Red"),
        (516, "Green"),
    ],
)
def test_p_30676(frequency: int, expected: str):
    assert p_30676(frequency) == expected


if __name__ == "__main__":
    frequency = int(input())
    print(p_30676(frequency))
