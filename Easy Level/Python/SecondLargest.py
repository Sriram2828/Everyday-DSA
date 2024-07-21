"""Challenge:
Given an array Arr of size N, print second largest distinct element from an array.

Your task is to complete the function print2largest() which takes the array of integers arr and n as parameters and returns an integer denoting the answer. 
If 2nd largest element doesn't exist then return -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Input: 
N = 6
Arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
Explanation: The largest element of the 
array is 35 and the second largest element
is 34.

"""
#Problem's link: https://www.geeksforgeeks.org/problems/second-largest/0

#Solution Code:
class Solution:
    def print2largest(self,arr, n):
        #if the length of the give array is less than 2 there won't be an second element 
        if(n<2):
            return -1
        #Initialize the starting element of the array as firstLargestElement. 
        firstLargerElement = arr[0]
        secondLargerElement = 0
        
        #Iterate and update the secondLargestElement. 
        for i in range(1,n): #Time Complexity: O(N)
            
            if(arr[i]>firstLargerElement):
                secondLargerElement = firstLargerElement
                firstLargerElement = arr[i]
                
            elif(arr[i]>secondLargerElement and arr[i]<firstLargerElement):
                secondLargerElement = arr[i]
        #If the secondLargestElement is greater than 0 return the value or else return -1.        
        if(secondLargerElement > 0):
            return secondLargerElement
        else:
            return -1
        
# Boilerplate Code:
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

"""
Result:
    For Input: 
    6
    12 35 1 10 34 1
    Your Output: 
    34
    Expected Output: 
    34   
"""

"""
Company Tags
SAP Labs, Rockstand

Topic Tags
Arrays, Searching, Data Structures, Algorithms
"""