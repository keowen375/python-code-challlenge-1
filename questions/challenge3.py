"""
    Challenge 3: Consonant value

    Given a lowercase string that has alphabetic characters 
    only and no spaces, return the highest value of consonant
    substrings. Consonants are any letters of the alphabet 
    except "aeiou".We shall assign the following values: 
    a = 1, b = 2, c = 3, .... z = 26.

    Examples;
        For the word "zodiacs", solve("zodiacs") = 26
            For example, for the word "zodiacs", let's cross out the 
            vowels. We get: "z d cs".

            -- The consonant substrings are: "z", "d" and "cs" and the values 
            are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.

        For the word "strength", solve("strength") = 57.
            The consonant substrings are: "str" and "ngth" with 
            values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49.
            The highest is 57.
"""

alphabetic_number_position = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

vowels = "aeiou"


def remove_vowels_from_string(lower_str):
    l_str_list = []
    l_str_list[:] = lower_str
    for i, c in enumerate(l_str_list):
        if (c in vowels):
            l_str_list[i] = " "
    return "".join(l_str_list)


def calculate_consonant_values(l_str):
    only_consonant_str = remove_vowels_from_string(l_str)
    constant_list_groups = only_consonant_str.split(" ")
    constant_list_of_char_list = [[c for c in s] for s in constant_list_groups]
    summed_list_values_for_list_of_contants = [
        sum(
            [alphabetic_number_position[c] for c in l]
        ) for l in constant_list_of_char_list if l != []
    ]

    return summed_list_values_for_list_of_contants


def find_maximum_consonant_value(lower_case_str):
    return max(calculate_consonant_values(lower_case_str))
