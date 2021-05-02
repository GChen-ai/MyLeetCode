class Solution {
    public int singleNumber(int[] nums) {
        HashSet<Integer> dic=new HashSet();
        long sum=0;
        long sum3=0;
        for (int i=0;i<nums.length;i++){
            sum3+=nums[i];
            if (dic.contains(nums[i])) continue;
            dic.add(nums[i]);
            sum+=nums[i];
        }
        return (int)((sum*3-sum3)/2);
    }
}