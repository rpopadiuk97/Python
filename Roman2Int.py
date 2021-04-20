class Solution(object):
    def romanToInt(str):

        sum = 0
        ValueOf = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        for i in range(len(str)):
            at = ValueOf[str[i]]
            before = ValueOf[str[i-1]]
            sum = sum + at
            if at > before and i!=0:
                sum = sum - 2*before
            print(sum)
        return sum