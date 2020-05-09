from find_numbers import Solution as sln

test_solution = sln()

def test_single_digit():
    return test_solution.getNumOfDigits(1) == 1

def test_double_digit():
    return test_solution.getNumOfDigits(12) == 2

def test_large_num_of_digits():
    return test_solution.getNumOfDigits(1234567890) == 10

def test_even_num_of_digits():
    return test_solution.isEvenNumOfDigits(12) == True

def test_odd_num_of_digits():
    return test_solution.isEvenNumOfDigits(123) == False

def test_zero():
    test_ary = [0]
    return test_solution.findNumbers(test_ary) == 0

def test_one_even():
    test_ary = [12]
    return test_solution.findNumbers(test_ary) == 1

def test_one_odd():
    test_ary = [112]
    return test_solution.findNumbers(test_ary) == 0

def test_all_evens():
    test_ary = [12, 34, 56]
    return test_solution.findNumbers(test_ary) == 3

def test_all_odds():
    test_ary = [1,2, 3,4]
    return test_solution.findNumbers(test_ary) == 0

def test_mixed():
    test_ary = [1, 23, 4, 5678, 90]
    return test_solution.findNumbers(test_ary) == 3

def main():
    print(test_single_digit())
    print(test_double_digit())
    print(test_large_num_of_digits())
    print(test_even_num_of_digits())
    print(test_odd_num_of_digits())
    print(test_zero())
    print(test_one_even())
    print(test_one_odd())
    print(test_all_evens())
    print(test_all_odds())
    print(test_mixed())


if __name__ == "__main__":
    main()
