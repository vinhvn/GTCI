"""

Problem:
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

Example:
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]

"""

# My solution
def average_of_subarrays(k: int, nums: list[int]) -> list[float]:
    # initializing empty list for output
    averages: list[float] = [None] * (len(nums) - k + 1)
    s = 0  # sum
    start_idx = 0
    for end_idx in range(len(nums)):
        s += nums[end_idx]  # add next element to window
        # slide window if window is size k
        if end_idx >= k - 1:
            averages[start_idx] = s / k
            s -= nums[start_idx]  # remove leftmost num from window
            start_idx += 1

    return averages


def run_tests():
    print("\nAverage of Subarrays of size k:\n")

    k = 5
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    expected = [2.2, 2.8, 2.4, 3.6, 2.8]
    actual = average_of_subarrays(k, arr)
    print(
        f"[TEST] inputs: k = {k}, arr = {arr}\nExpected: {expected}\nActual: {actual}\nEqual? {expected == actual}\n"
    )

    k = 3
    arr = [100, 150, 50, 10, 0, 8, 1]
    expected = [100.0, 70.0, 20.0, 6.0, 3.0]
    actual = average_of_subarrays(k, arr)
    print(
        f"[TEST] inputs: k = {k}, arr = {arr}\nExpected: {expected}\nActual: {actual}\nEqual? {expected == actual}\n"
    )

    k = 10
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = [5.5, 6.5, 7.5]
    actual = average_of_subarrays(k, arr)
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
The space complexity of my solution is O(n).
An array is required to store and return the averages, which will always be O(n-k) in length, which is asymptotically equal to O(n).

"""
