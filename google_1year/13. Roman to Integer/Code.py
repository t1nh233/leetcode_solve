class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I" : 1, 
                 "V" : 5, 
                 "X" : 10, 
                 "L" : 50, 
                 "C" : 100, 
                 "D" : 500, 
                 "M" : 1000
            }
        res = 0
        prev_val = 0
        for sym in reversed(s):
            if roman[sym] < prev_val:
                res -= roman[sym]
            else:
                res += roman[sym]
            prev_val = roman[sym]
        return res
