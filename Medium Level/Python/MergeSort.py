"""Challenge:
Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.
Your task is to complete the function merge() which takes arr[], l, m, r as its input parameters and modifies arr[] in-place such that it is sorted from position l to position r, and function mergeSort() which uses merge() to sort the array in ascending order using merge sort algorithm.

Expected Time Complexity: O(nlogn) 
Expected Auxiliary Space: O(n)

Input:
N = 5
arr[] = {4 1 3 9 7}
Output:
1 3 4 7 9
"""
#Problem's link: https://www.geeksforgeeks.org/problems/merge-sort/0

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
            
    # Recursive functions to separate the individual elements of the given array
    def mergeSort(self,arr, l, r):
        # if the starting position of the recursive function is greater than or equal to the ending position 
        #then the recursive function call should be terminated (return nothing)
        if(l>=r):
            return 
        # Calculating the middle position which separate the given array into two subarray
        m = (l+r)//2
        # Recursively separate the left subarray into individual separate element 
        Solution.mergeSort(self,arr,l,m)
        # Recursively separate the right subarray into individual separate element 
        Solution.mergeSort(self,arr,m+1,r)
        # Calling the merge function to merge the all the separated element into a single sorted array
        Solution.merge(self,arr,l,m,r)

# Boilerplate Code:
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

"""
Result:
    For Input: 
    5
    4 1 3 9 7
    Your Output: 
    1 3 4 7 9
    Expected Output: 
    1 3 4 7 9
"""

"""
Company Tags:
Paytm, Amazon, Microsoft, Snapdeal, Oracle, Wipro, etc...,

Topic Tags:
Divide and Conquer, Sorting, Algorithms

"""
