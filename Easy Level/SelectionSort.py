"""Challenge:
Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.

Complete the functions select() and selectionSort(), where select() takes arr[] and starting point of unsorted array i as input parameters 
and returns the selected element for each iteration in selection sort, and selectionSort() takes the array and it's size and sorts the array.

Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(1)

Input:
N = 5
arr[] = {4, 1, 3, 9, 7}
Output:
1 3 4 7 9
Explanation:
Maintain sorted (in bold) and unsorted subarrays.
Select 1. Array becomes 1 4 3 9 7.
Select 3. Array becomes 1 3 4 9 7.
Select 4. Array becomes 1 3 4 9 7.
Select 7. Array becomes 1 3 4 7 9.
Select 9. Array becomes 1 3 4 7 9.
"""
#Problem's link: https://www.geeksforgeeks.org/problems/selection-sort/0

#Solution Code:
class Solution: 
    #code to sort the array by comparing and swapping 
    def select(self, arr, i):
        
        #Initially the minimum element is the i from the selectionSort()
        minElement = i
        #this loop will iterate through the array and update the minimum element
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[minElement]):
                minElement = j
        #Swap the minimum element of the array with the i'th element of the array
        arr[i],arr[minElement] = arr[minElement],arr[i]
        
    def selectionSort(self, arr,n):
        #code to select the sequential element in the array for comparison with the minimum element in the array
        for i in range(n-1):
            #self keyword refers to the instance of the class (function inside the same class)
            self.select(arr, i)

# Boilerplate Code:
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
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
Microsoft, Medlife

Topic Tags
Sorting, Algorithms
"""