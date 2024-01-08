"""Challenge:
Given a number and its reverse. Find that number raised to the power of its own reverse.
Note: As answers can be very large, print the result modulo 109 + 7.

You just need to complete the function pow() that takes two parameters N and R 
denoting the input number and its reverse and returns power of (N to R)mod(109 + 7).

Expected Time Complexity: O(LogN).
Expected Auxiliary Space: O(LogN).

Input:
N = 2, R = 2
Output: 4
Explanation: 
The reverse of 2 is 2 and after raising power of 2 by 2 we get 4 
which gives remainder as 4 when divided by 1000000007.
"""
#Problem's link: https://www.geeksforgeeks.org/problems/power-of-numbers/0

#Solution Code:
class Solution:
    def power(self,N,R):
        #Variable declaration
        result = 1
        mod = (10**9)+7 #mod = 1000000007
        while (R > 0):
            if (R%2==1):
                result = (result*N) % mod
            N = (N*N) % mod
            R //= 2
        return result 
      
# Boilerplate Code:
import math
def main():
    T=int(input())
    while(T>0):
        N=input()
        R=N[::-1]
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        T-=1
if __name__=="__main__":
    main()

"""
Result:
    For Input: 
    2
    Your Output: 
    4
    Expected Output: 
    4
"""

"""
Company Tags
MakeMyTrip, Walmart

Topic Tags
Mathematical, Recursion, Divide and Conquer, Algorithms

"""