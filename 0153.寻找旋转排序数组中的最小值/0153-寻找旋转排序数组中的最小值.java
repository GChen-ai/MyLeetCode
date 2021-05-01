class Solution {
    public int findMin(int[] nums) {
        if (nums==null || nums.length==0) return 0;
        int left=0;
        int right=nums.length-1;
        int result=0;
        if (nums[left]<=nums[right]) return nums[left];
        while(left<right){
            int mid=(left+right)/2;
            if(nums[mid]>nums[right]){
                left=mid+1;
            }else{
                right=mid;
            }
        }
        return nums[left];
    }
}