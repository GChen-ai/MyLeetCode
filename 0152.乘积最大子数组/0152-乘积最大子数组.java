class Solution {
    public int maxProduct(int[] nums) {
        if (nums==null || nums.length==0) return 0;
        int max=nums[0];
        int maxtemp=1;
        int mintemp=1;
        for (int i=0;i<nums.length;i++){
            if (nums[i]<0){
                int temp=maxtemp;
                maxtemp=mintemp;
                mintemp=temp;
            }
            maxtemp=Math.max(nums[i]*maxtemp,nums[i]);
            mintemp=Math.min(nums[i]*mintemp,nums[i]);
            max=Math.max(max,maxtemp);
        }
        return max;
    }
}