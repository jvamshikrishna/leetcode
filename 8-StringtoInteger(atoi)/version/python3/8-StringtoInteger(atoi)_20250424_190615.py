# Last updated: 4/24/2025, 7:06:15 PM
class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        n = len(s)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # step 1: skip the whietspaces
        while i< n and s[i] == ' ':
            i+=1
        
        #step 2: handle the sign
        sign = 1
        if i<n and (s[i]=='+' or s[i]=='-'):
            if s[i]== '-':
                sign = -1
            i+=1
        
        #step 3: convert digit to integer
        result = 0
        while i<n and s[i].isdigit():
            result = result*10 + int(s[i])
            i+=1

        result = result * sign

        #step 4: check if its in range of 32 bit
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result




        