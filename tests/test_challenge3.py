from questions.challenge3 import (
    remove_vowels_from_string,
    calculate_consonant_values,
    find_maximum_consonant_value
)


def test_remove_vowels_from_string():
    """
    Test removing vowels from string
    """

    str_result1 = remove_vowels_from_string("zodiacs")
    str_result2 = remove_vowels_from_string("strength")

    assert str_result1 == "z d  cs"
    assert str_result2 == "str ngth"


def test_calculate_consonant_values():
    """
    Test calculating constant int values
    """

    result1 = calculate_consonant_values("zodiacs")
    result2 = calculate_consonant_values("strength")

    assert result1 == [26, 4, 22]
    assert result2 == [57, 49]


def test_find_maximum_consonant_value():
    """
    Test finding maximum constant int value
    """

    result1 = find_maximum_consonant_value("zodiacs")
    result2 = find_maximum_consonant_value("strength")

    assert result1 == 26
    assert result2 == 57
