class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
        List<Integer> result=new ArrayList();
        for (int i=0;i<nums.length;i++){
            while(nums[nums[i]-1]!=nums[i]){
                //System.out.println(nums[i]);
                int temp=nums[nums[i]-1];
                nums[nums[i]-1]=nums[i];
                nums[i]=temp;
            }
        }
        for (int i=0;i<nums.length;i++){
            //System.out.println(nums[i]);
            if (nums[i]!=i+1){
                result.add(i+1);
            }
        }
        return result;
    }
}
