"""
Practice for bitwise operations

Write a function that checks if the binary representation of an integer is a palindrome

"""

test_set = {
    1: True,
    2: False,
    3: True,
    4: False,
    5: True,
    6: False,
    7: True,
    128: False,
    200: False,
    342: False,
    17: True,
    18: False
}

def is_binary_palindrome(num: int) -> bool:
    """
    returns True if the two's complement binary representation of num is a palindrome, else returns False
    """
    # convert the num to a literal string of it's bits, removing the first two characters that denote binary rep [0b]
    bitstring = bin(num)[2:]
    
    # if the bitstring is equal to it's reverse it's a palindrome, return True
    if bitstring == bitstring[::-1]:
        return True

    # if they aren't equal the bitstring isn't a palindrome, return False
    return False


def test_is_binary_palindrome(test_set: dict, ) -> bool:
    results = []

    # loop through the test set and print the results
    for test_num, correct_answer in test_set.items():
        this_result = is_binary_palindrome(test_num)
        is_correct = this_result == correct_answer
        results.append(is_correct)
        print('Test is_binary_palindrome({0}) returned {1}, correct is {2}'.format(test_num, this_result, correct_answer))

    if False not in results:
        print('All test cases passed.')

test_is_binary_palindrome(test_set)