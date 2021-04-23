"""

Problem:
Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of size 'k'.

Example:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

"""

# My solution
def find_max_sum_subarray(k: int, arr: list[int]) -> int:
    max_sum = 0
    s = 0  # sum
    start_idx = 0
    for end_idx in range(len(arr)):
        s += arr[end_idx]  # add next elem to window
        # slide window
        if end_idx >= k - 1:
            if s > max_sum:  # keep track of max
                max_sum = s
            s -= arr[start_idx]  # remove leftmost num from window
            start_idx += 1

    return max_sum


# Their solution
def find_max_sum_subarray_soln(k: int, arr: list[int]) -> int:
    max_sum = 0
    s = 0
    start_idx = 0
    for end_idx in range(len(arr)):
        s += arr[end_idx]  # add next elem to window
        # slide window
        if end_idx >= k - 1:
            max_sum = max(max_sum, s)
            s -= arr[start_idx]  # remove leftmost num from window
            start_idx += 1

    return max_sum


def run_tests():
    print("\nMaximum Sum Subarray of Size K:\n")

    k = 3
    arr = [2, 1, 5, 1, 3, 2]
    expected = find_max_sum_subarray_soln(k, arr)
    actual = find_max_sum_subarray(k, arr)
    print(
        f"[TEST] inputs: k = {k}, arr = {arr}\nExpected: {expected}\nActual: {actual}\nEqual? {expected == actual}\n"
    )

    k = 2
    arr = [2, 3, 4, 1, 5]
    expected = find_max_sum_subarray_soln(k, arr)
    actual = find_max_sum_subarray(k, arr)
    print(
        f"[TEST] inputs: k = {k}, arr = {arr}\nExpected: {expected}\nActual: {actual}\nEqual? {expected == actual}\n"
    )


if __name__ == "__main__":
    run_tests()

"""

Time complexity:
The runtime complexity of my solution is O(n).
The for loop runs n times and the work done inside is constant, processing each element only once, leading to an O(n) algorithm.

Space complexity:
The space complexity of my solution is O(1).
The only space used is in the variables to store the sum and max sum, which are both constant and do not grow or shrink, resulting in a constant space solution of O(1).

"""
