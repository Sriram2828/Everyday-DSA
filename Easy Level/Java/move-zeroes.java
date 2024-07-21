// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.

class Solution {
    public void moveZeroes(int[] nums) {
        // shift all non-zeros to the front
        int c = 0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=0){
                nums[c++] = nums[i];
            }
        }
        // add all zeros till the end of the array
        while(c<nums.length){
            nums[c++]=0;
        }
        System.out.println(nums);
    }
}