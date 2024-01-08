"""Challenge:
Given a number N, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number. 
Return 1 if the number is Perfect otherwise return 0.

Your task is to complete the function isPerfectNumber() which takes an Integer N as input and returns 1 if N is a Perfect number else returns 0.

Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)

Input:
N = 6
Output:
1 
Explanation:
Factors of 6 are 1, 2, 3 and 6.
Excluding 6 their sum is 6 which
is equal to N itself. So, it's a
Perfect Number.

"""
#Problem's link: https://www.geeksforgeeks.org/problems/perfect-numbers3207/0

#Solution Code:
class Solution:
    def isPerfectNumber(self, N):
        # if the given number is less than or equal to 1 that is not a perfect number
        if(N<=1):
            return 0
        verify = N
        res = 1
        for i in range(2,int(N**0.5)+1): #Time Complexity: O(sqrt(N))
             if(N%i == 0):
                 res += i
                 if(i != N//i): 
                     res += N//i
        #if the sum of the factors are equal to the given integer the given integer is a perfect number
        if(res == verify):
            return 1
        else:
            return 0
        
# Boilerplate Code:
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        ob = Solution()
        print(ob.isPerfectNumber(N))

"""
Result:
    For Input: 
    6
    Your Output: 
    1
    Expected Output: 
    1
"""

"""
Company Tags:
Wipro

Topic Tags:
Mathematical, Algorithms
"""