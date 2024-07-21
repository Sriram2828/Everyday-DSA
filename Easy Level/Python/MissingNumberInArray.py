"""Challenge:
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.
Complete the function MissingNumber() that takes array and N as input  parameters and returns the value of the missing number.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Input:
N = 5
A[] = {1,2,3,5}
Output: 4
"""
#Problem's link: https://www.geeksforgeeks.org/problems/missing-number-in-array/0

#Solution Code:
class Solution:
    def missingNumber(self,array,n):
        #The Verify variable is to verify the final sum for the given array in a range of (1 to n). which have the missing value.
        Verify = (n*(n+1))/2
        SumofArrayElements = 0 # To store the sum of all element in the given array
        for i in range(n-1): # Time Complexity: O(N)
            SumofArrayElements += array[i]
        result = int(Verify - SumofArrayElements)

        return result # To return the missing value 

# Boilerplate Code:
t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)

"""
Result:
    For Input: 
    5
    1 2 3 5
    Your Output: 
    4
    Expected Output: 
    4
"""

"""
Company Tags
Flipkart, Amazon, Microsoft, Ola Cabs, Cisco, etc..,

Topic Tags
Arrays, Searching, Bit Magic, Data Structures, Algorithms

"""