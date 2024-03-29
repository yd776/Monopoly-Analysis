class Solution:
    # @param A: tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return 0

        max_sum = A[0]  # Initialize max_sum to the first element
        current_sum = A[0]  # Initialize current_sum to the first element

        for num in A[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
