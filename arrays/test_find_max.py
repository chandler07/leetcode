from find_max_consecutive_ones import Solution as sln

test_solution = sln()

def test_zero():
    test_ary = [0]
    return test_solution.findMaxConsecutiveOnes(test_ary) == 0

def test_one():
    test_ary = [1]
    return test_solution.findMaxConsecutiveOnes(test_ary) == 1

def test_multiple():
    test_ary = [1, 0, 1, 1]
    return test_solution.findMaxConsecutiveOnes(test_ary) == 2

def test_increasing():
    test_ary = [0,1,1, 1]
    return test_solution.findMaxConsecutiveOnes(test_ary) == 3

def test_decreasing():
    test_ary = [1, 1, 1, 1, 0]
    return test_solution.findMaxConsecutiveOnes(test_ary) == 4

def test_max_first():
    test_ary = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
    return test_solution.findMaxConsecutiveOnes(test_ary) == 4

def test_max_last():
    test_ary = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1 , 1]
    return test_solution.findMaxConsecutiveOnes(test_ary) == 5

def test_max_middle():
    test_ary = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    return test_solution.findMaxConsecutiveOnes(test_ary) == 5


def main():
    print(test_zero())
    print(test_one())
    print(test_multiple())
    print(test_increasing())
    print(test_decreasing())
    print(test_max_first())
    print(test_max_last())
    print(test_max_middle())


if __name__ == "__main__":
    main()