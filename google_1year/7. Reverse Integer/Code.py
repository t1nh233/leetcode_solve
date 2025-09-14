class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > 7):
                return 0
            res = res * 10 + pop
        res *= sign
        return res if INT_MIN <= res <= INT_MAX else 0
