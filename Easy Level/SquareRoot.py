"""Challenge: 
Given an integer x, find the square root of x.If x is not a perfect square, then return floor(√x).
The task is to complete the function floorSqrt() which takes x as the input parameter and return its square root.

Note: Try Solving the question without using the sqrt function. The value of x>=0.

Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)

Input:
x = 5
Output: 2
Explanation: Since, 5 is not a perfect 
square, floor of square_root of 5 is 2.

"""
#Problem's link: https://www.geeksforgeeks.org/problems/square-root/0

#Solution Code: (Binary search approach -> Time Complexity: O(log N))
class Solution:
    def floorSqrt(self, x): 
        # Variable declaration
        low = 1
        high = x
        result = 1

        while (low <= high):
            mid = (low+high)//2
            tempmid = mid
            if(mid*tempmid<=x): #Binary search check statement
                result = mid
                low = mid+1
            else:
                high = mid-1
        return result
    
#Boilerplate Code:
import math
def main():
        T=int(input())
        while(T>0):
            x=int(input())
            print(Solution().floorSqrt(x))
            T-=1
if __name__ == "__main__":
    main()

"""
Result:
    Input: 
    145
    Your Output: 
    12
    Expected Output: 
    12
"""

"""
Company Tags:
VMWare, Flipkart, Accolite, Amazon, Microsoft

Topic Tags:
Searching, Mathematical, Binary Search, Algorithms
"""