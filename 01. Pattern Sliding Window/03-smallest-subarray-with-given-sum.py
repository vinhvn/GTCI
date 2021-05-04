"""

Problem:
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Examples:

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

"""

# My solution
def smallest_subarray_with_given_sum(S: int, arr: list[int]) -> int:
    res = len(arr) + 1 # length
    s = 0  # sum
    window_size = 1
    start_idx = 0
    for end_idx in range(len(arr)):
        s += arr[end_idx]
        while s >= S:
            res = min(res, end_idx - start_idx + 1)
            s -= arr[start_idx]
            start_idx += 1

    if res == len(arr) + 1:
        return 0

    return res


import math

# Their solution
def smallest_subarray_with_given_sum_soln(S: int, arr: list[int]) -> int:
    window_sum = 0
    min_length = math.inf
    window_start = 0

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end] # add the next element
        # shrink the window as small as possible until the window sum is smaller than s
        while window_sum >= S:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    
    if min_length == math.inf:
        return 0

    return min_length


def run_tests():
    print("\nSmallest Subarray with a given sum:\n")

    S = 7
    arr = [2, 1, 5, 2, 3, 2]
    expected = smallest_subarray_with_given_sum_soln(S, arr)
    actual = smallest_subarray_with_given_sum(S, arr)
    print(
        f"[TEST] inputs: S = {S}, arr = {arr}\nExpected: {expected}\nActual: {actual}\nEqual? {expected == actual}\n"
    )

    S = 7
    arr = [2, 1, 5, 2, 8]
    expected = smallest_subarray_with_given_sum_soln(S, arr)
    actual = smallest_subarray_with_given_sum(S, arr)
    print(
        f"[TEST] inputs: S = {S}, arr = {arr}\nExpected: {expected}\nActual: {actual}\nEqual? {expected == actual}\n"
    )

    S = 8
    arr = [3, 4, 1, 1, 6]
    expected = smallest_subarray_with_given_sum_soln(S, arr)
    actual = smallest_subarray_with_given_sum(S, arr)
    print(
        f"[TEST] inputs: S = {S}, arr = {arr}\nExpected: {expected}\nActual: {actual}\nEqual? {expected == actual}\n"
    )


if __name__ == "__main__":
    run_tests()

"""

Time complexity:
The runtime complexity of my solution is O(n).
The for loop runs n times and the inner while loop both process each element only once, leading to an O(n+n) = O(2n) = O(n) algorithm.

Space complexity:
The space complexity of my solution is O(1).
The only space used is in the variables to store the sum and length, which are both constant and do not grow or shrink, resulting in a constant space solution of O(1).

"""
