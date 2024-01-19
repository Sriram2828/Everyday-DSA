"""Challenge:
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Your task is to complete the function inversionCount() which takes the array arr[] and the size of the array as inputs and returns the inversion count of the given array.

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).

Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).
"""
#Problem's link: https://www.geeksforgeeks.org/problems/inversion-of-array/0

#Solution Code:
class Solution:
    # Function to merge the separated elements of the array in a sorted order
    def merge(self,arr, l, m, r): 
        # Temporary array to merge the sorting element from the two subarrays
        temp = []
        # Left variable to store the initial position of the array
        left = l
        # Right variable to store the last position of the array
        right = m+1
        # Count variable is to count the inversionset in the given array
        count = 0
        # Loop to sort and store the elements until the one array of the two subarrays stored completely 
        while(left <= m and right <= r):
            # if the pointed element of the left subarray is lesser than the right one 
            # then the element of the left subarray which is pointed will be append to the temp[]
            # and the pointing position of the left array will be move to the next element 
            if(arr[left]<=arr[right]):
                temp.append(arr[left])
                left += 1
            # else the element of the right subarray which is pointed will be append to the temp[]
            # and the pointing position of the right subarray will be move to the next element 
            else:
                temp.append(arr[right])
                # counting the inversionset using the left subset
                count += (m - left + 1)
                right += 1
        # if there is any extra element in the left subarray which is not appended to the temp[]
        # will be appended in this iteration
        while(left <= m):
            temp.append(arr[left])
            left += 1
        # if there is any extra element in the right subarray which is not appended to the temp[]
        # will be appended in this iteration
        while(right <= r):
            temp.append(arr[right])
            right += 1
        # All the sorted and merged elements in the temp[] will be then transferred to the arr[] which is given in the problem
        for i in range(l,r+1):
            arr[i] = temp[i-l]
        # return the inversion count value of the array
        return count
            
    # Recursive functions to separate the individual elements of the given array
    def mergeSort(self,arr, l, r):
        # initialize the count variable
        count = 0
        # if the starting position of the recursive function is greater than or equal to the ending position 
        #then the recursive function call should be terminated (return count value)
        if(l>=r):
            return count 
        # Calculating the middle position which separate the given array into two subarray
        m = (l+r)//2
        # Recursively separate the left subarray into individual separate element and add the value to the count 
        count += Solution.mergeSort(self,arr,l,m)
        # Recursively separate the right subarray into individual separate element and add the value to the count 
        count += Solution.mergeSort(self,arr,m+1,r)
        # Calling the merge function to merge the all the separated element into a single sorted array
        # and add the value to the count 
        count += Solution.merge(self,arr,l,m,r)
        
        # return the inversion count value of the array
        return count

    def inversionCount(self, arr, n):
        # Return the final count of the inversion set
        return Solution.mergeSort(self,arr,0,n-1)
        
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
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))

"""
Result:
    For Input: 
    5
    2 4 1 3 5
    Your Output: 
    3
    Expected Output: 
    3
"""

"""
Company Tags
Flipkart, Amazon, Microsoft, MakeMyTrip, Adobe, BankBazaar, Myntra

Topic Tags
Arrays, Divide and Conquer, Sorting, Data Structures, Algorithms

"""