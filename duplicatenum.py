def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """

    curr_sum = 0
    diff_sum =0
    for item in arr:
        curr_sum+=item
    for item in range(len(arr)-1):
        diff_sum+=item
    return curr_sum-diff_sum
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [0, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3

test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)