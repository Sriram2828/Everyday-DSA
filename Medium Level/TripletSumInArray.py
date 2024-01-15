"""Challenge:
Given an array arr of size n and an integer X. 
Find if there's a triplet in the array which sums up to the given integer X.

Your task is to complete the function find3Numbers() which takes the array arr[], the size of the array (n) and the sum (X) as inputs and returns True if there exists a triplet in the array arr[] which sums up to X and False otherwise.

Expected Time Complexity: O(n^2)
Expected Auxiliary Space: O(1)

Input:
n = 6, X = 13
arr[] = [1 4 45 6 10 8]
Output:
1
Explanation:
The triplet {1, 4, 8} in 
the array sums up to 13.
"""
#Problem's link: https://www.geeksforgeeks.org/problems/triplet-sum-in-array/0

#Solution Code:[solve the problem using two pointer method]
class Solution:
    def find3Numbers(self,A, n, X):
        # sort the given array
        A.sort()

        for i in range(n-2):
            # initialize the left and right pointers
            left = i + 1 # points next to the starting element of the given array
            right = n - 1 # points last element od the given array
    
            # loop runs until the left and right pointer crosses or points to the same element of the array
            while left < right:
                # generate the triplet sum using the iterated elements of the array
                current_sum = A[i] + A[left] + A[right]
                
                # if the generated triplet sum is equal to the given sum value X return true
                if current_sum == X:
                    return True
                    
                # if the generated triplet sum is lesser then move the left pointer to next element
                elif current_sum < X:
                    left += 1
                    
                # if the generated triplet sum is greater then move the right pointer to next element to the left
                else:
                    right -= 1
        
        # if all the condition is not satisfied throughout the loop then return false
        return False
    
# Boilerplate Code:
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)

"""
Result:
    For Input: 
    6 13
    1 4 45 6 10 8
    Your Output: 
    1
    Expected Output: 
    1
"""

"""
Company Tags
Accolite, Amazon, Microsoft, OYO Rooms, Samsung, CarWale

Topic Tags
two-pointer-algorithm, Arrays, Hash, Sorting, Data Structures, Algorithms

"""