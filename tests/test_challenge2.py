from questions.challenge2 import check_params_contain_two_positive_numbers


def test_check_params_contain_two_positive_numbers_returns_true():
    """
        Test check_params_contain_two_positive_numbers(a, b, c) returns True.
        Two positive arguments are passed.
    """
    result1 = check_params_contain_two_positive_numbers(2, 4, -3)
    result2 = check_params_contain_two_positive_numbers(-4, 6, 8)
    result3 = check_params_contain_two_positive_numbers(4, -6, 9)

    assert result1 == True, "Should return true"
    assert result2 == True, "Should return true"
    assert result3 == True, "Should return true"


def test_check_params_contain_two_positive_numbers_returns_false():
    """
        Test check_params_contain_two_positive_numbers(a, b, c) returns false.
    """
    result1 = check_params_contain_two_positive_numbers(-4, 6, 0)
    result2 = check_params_contain_two_positive_numbers(4, 6, 10)
    result3 = check_params_contain_two_positive_numbers(-14, -3, -4)

    assert result1 == False, "Should return false"
    assert result2 == False, "Should return false"
    assert result3 == False, "Should return false"
