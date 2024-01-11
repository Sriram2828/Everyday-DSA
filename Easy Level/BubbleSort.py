"""Challenge:
Given an Integer N and a list arr. Sort the array using bubble sort algorithm.

Your task is to complete the function bubblesort() which takes the array and it's size as input and sorts the array using bubble sort algorithm.

Expected Time Complexity: O(N^2).
Expected Auxiliary Space: O(1).

Input: 
N = 5
arr[] = {4, 1, 3, 9, 7}
Output: 
1 3 4 7 9
"""
#Problem's link: https://www.geeksforgeeks.org/problems/bubble-sort/0 

#Solution Code:
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        for i in range(n-1,0,-1): # i variable is used to decrease the array length by considering only the unsorted elements in the array
            for j in range(i):    # j variable is used to compare the variable in the unsorted array to swap the position 
                if(arr[j]>arr[j+1]): #Condition to check the element is greater than the next element in the array
                    arr[j], arr[j+1] = arr[j+1], arr[j] #Swapping operation

# Boilerplate Code:
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
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
Company Tags
Microsoft, Wipro, SAP Labs, Cisco, Nagarro, redBus, Accenture, Huawei

Topic Tags
Sorting, Algorithms

"""