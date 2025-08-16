class Solution:
    def maximum69Number(self, num: int) -> int:
        a = list(str(num))              # keep digits as string list
        for i in range(len(a)):
            if a[i] == '6':             # first '6'
                a[i] = '9'              # flip it
                break                   # only one change allowed
        return int("".join(a))
