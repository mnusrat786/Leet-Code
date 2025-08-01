class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]
        # if x < 0: return False
        # return str(x) == str(x)[::-1]    



        