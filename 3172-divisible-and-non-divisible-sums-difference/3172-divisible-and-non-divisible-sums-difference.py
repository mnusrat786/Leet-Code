class Solution(object):
    def differenceOfSums(self, n, m):
        num1 = 0  # sum of numbers not divisible by m
        num2 = 0  # sum of numbers divisible by m
        
        for i in range(1, n + 1):  # loop from 1 to n inclusive
            if i % m == 0:         # if i divisible by m
                num2 += i          # add it to num2
            else:
                num1 += i          # otherwise add it to num1
                
        return num1 - num2         # final result


        