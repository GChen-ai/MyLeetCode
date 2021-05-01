class Solution {
    public int arrayPairSum(int[] nums) {
        if (nums==null || nums.length==0) return 0;
        Arrays.sort(nums);
        int result=0;
        for (int i=0;i<nums.length;i+=2){
            result+=nums[i];
        }
        return result;
    }
}