"""Challenge:
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

Your task is to complete the function sort012() that takes an array arr and N as input parameters and sorts the array in-place.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
"""
#Problem's link: https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0

#Solution Code:
class Solution:
    def sort012(self,arr,n):
        #Variable declaration
        #Initially the low,mid are pointed to the starting position and high to the ending of an array
        low = 0
        high = n-1
        mid = 0
        
        #When the mid value and high value were equal the loop gets terminated
        while(mid <= high): 
            #when the array of mid value is 0, it should move to the next Left position of the iteration which is low
            #then the low and mid should be incremented
            if(arr[mid] == 0):
                temp = arr[low]
                arr[low] = arr[mid]
                arr[mid] = temp
                low += 1
                mid += 1
            #when the array of mid value is 1, it should stay in the same position
            #then the mid should be incremented
            elif(arr[mid] == 1):
                mid += 1
            #when the array of mid value is 2, it should move to the next right position of the iteration which is high
            #then the high should be decremented
            else:
                temp = arr[high]
                arr[high] = arr[mid]
                arr[mid] = temp
                high -= 1

        #sorted array
        return arr 

# Boilerplate Code:
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

"""
Result:
    For Input: 
    5
    0 2 1 2 0
    Your Output: 
    0 0 1 2 2
    Expected Output: 
    0 0 1 2 2
"""

"""
Company Tags
Paytm, Flipkart, Amazon, Microsoft, Samsung, Snapdeal, etc..,

Topic Tags
Arrays, Sorting, Data Structures, Algorithms
"""