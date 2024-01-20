"""Challenge:
Given an array containing N integers and an integer K., 
Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value K.

This is a function problem. The input is already taken care of by the driver code.
You only need to complete the function lenOfLongSubarr() that takes an array (A), sizeOfArray (n),  sum (K)and returns the required length of the longest Sub-Array. The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Input :
A[] = {10, 5, 2, 7, 1, 9}
K = 15
Output : 4
Explanation:
The sub-array is {5, 2, 7, 1}.
"""
#Problem's link: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k/0

#Solution Code:
class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        # hashmap to store the position of the sum k
        hashMap = {}
        # sum variable to add the element in the iteration
        Sum = 0
        # maxlength variable is to store the length of the longest subarray with the sum k 
        maxLength = 0
        
        # iterate through the array to find the longest subarray 
        for i in range(n):
            # calculate the prefix sum 
            Sum += arr[i]
            
            # check the generated sum is equal to the given sum
            if(Sum == k):
                # to find the longest subarray length which is equal to the given sum k
                maxLength = max(maxLength, i+1)
                
            # calculate the sum of remaining part
            remaining = Sum - k
            # check if the remaining is in the hashmap 
            # if it is in the map 
            if remaining in hashMap:
                # calculate the subarray length 
                length = i - hashMap[remaining]
                # update the maxlength 
                maxLength = max(maxLength, length)
            # if the sum is not stored in the hashmap store the sum as a key and the value as the index of the last element of the subarray
            if Sum not in hashMap:
                hashMap[Sum] = i
        
        # finally return the maxlength
        return maxLength
    
# Boilerplate Code:
for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))


"""
Result:
    For Input: 
    6 16
    1 4 3 3 5 5
    Your Output: 
    5
    Expected Output: 
    5
"""

"""
Company Tags:
Amazon

Topic Tags
sliding-window, Arrays, HashMap, Data Structures, Algorithms

"""