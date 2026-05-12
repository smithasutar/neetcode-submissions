class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        mid = n // 2
        right = n - 1

        for i in range(mid):
            s[i], s[right] = s[right], s[i]
            right -= 1