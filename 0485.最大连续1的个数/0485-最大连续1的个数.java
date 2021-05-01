class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        if (nums==null || nums.length==0) return 0;
        int result=0;
        int temp=0;
        for (int i=0;i<nums.length;i++){
            if (nums[i]==0){
                result=Math.max(result,temp);
                temp=0;
            }else{
                temp++;
            }
        }
        result=Math.max(result,temp);
        return result;
    }
}