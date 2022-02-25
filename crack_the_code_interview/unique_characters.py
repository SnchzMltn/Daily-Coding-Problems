"""
Is Unique:

    implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data
    structures?
"""

test_suite = ["implement", "an", "algorithm", "to", "determine", "if", "a"]


def brute_force(word):
    """
    Iterate for each character in the string and iterate over the rest of the string.
    If any count is > 1 the string (word) would be invalid.
    :param word: string input to validate
    :return: true if String has all unique characters
    """
    for i, char in enumerate(word):
        print(i, ", ", char)
        word_as_list = list(word)
        for j, other_char in enumerate(word_as_list[1:len(word_as_list)]):
            print(j, ", ", other_char)
            if char == other_char:
                return False
    return True


def pointers(word):
    pass


print(brute_force(test_suite[1]))
