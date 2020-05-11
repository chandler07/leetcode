from sorted_squares import Solution as sln

test_solution = sln()

def test_zero():
    test_ary  = [0]
    return test_solution.sortedSquares(test_ary) == [0]

def test_one():
    test_ary = [1]
    return test_solution.sortedSquares(test_ary) == [1]

def test_all_zeros():
    test_ary = [0,0,0,0,0]
    return test_solution.sortedSquares(test_ary) == [0, 0, 0, 0, 0]

def test_all_ones():
    test_ary = [1, 1, 1, 1, 1]
    return test_solution.sortedSquares(test_ary) == [1, 1, 1, 1, 1]

def test_all_positive():
    test_ary = [1, 2, 3, 4, 5]
    return  test_solution.sortedSquares(test_ary) == [1, 4, 9, 16, 25]

def test_all_negative():
    test_ary = [-5, -4, -3, -2, -1]
    return test_solution.sortedSquares(test_ary) == [1, 4, 9, 16, 25]

def test_mixed():
    test_ary = [-4, -1, 0, 3, 10]
    return test_solution.sortedSquares(test_ary) == [0, 1, 9, 16, 100]

def test_mixed_with_repeats():
    test_ary = [-7, -3, 2, 3, 11]
    return test_solution.sortedSquares(test_ary) == [4, 9, 9, 49, 121]


def main():
    print(test_zero())
    print(test_one())
    print(test_all_zeros())
    print(test_all_ones())
    print(test_all_positive())
    print(test_all_negative())
    print(test_mixed())
    print(test_mixed_with_repeats())

if __name__ == "__main__":
    main()
