"""
https://leetcode.com/problems/duplicate-zeros/

Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

 

Note:

    1 <= arr.length <= 10000
    0 <= arr[i] <= 9

"""

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # no 0's, no mods
        if 0 not in arr:
            print("no 0's")
            return
        
        skipNext = False # make sure we don't count the same 0 twice
        for i, num in enumerate(arr):
            if num == 0 and not skipNext:
                arr.insert(i, 0)
                arr.pop() # remove the last element after inserting effectively shifts right
                skipNext = True
            else:
                skipNext = False

test_cases = [
    ([1,0,2,3,0,4,5,0], [1,0,0,2,3,0,0,4]),
    ([1,2,3], [1,2,3])
]

solution = Solution()
for i, case in enumerate(test_cases):
    solution.duplicateZeros(case[0])
    if (case[0] == case[1]):
        print("Test Case {0}: passed".format(i, case[0]))
    else:
        print("Test Case {0}: failed (got {1}, expected: {2})".format(i, case[0], case[1]))

