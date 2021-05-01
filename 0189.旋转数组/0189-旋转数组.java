class Solution {
    public void rotate(int[] nums, int k) {
        if (nums==null || nums.length<=1 || k<=0) return;
        k=k%nums.length;
        if (k==0) return;
        int[] old=new int[k];
        for (int j=0;j<k;j++){
            old[j]=nums[nums.length-k+j];
        }
        int temp=0;
        for (int i=0;i<nums.length;i+=k){
            for(int j=0;j<k;j++){
                if (i+j>=nums.length) break;
                temp=nums[i+j];
                nums[i+j]=old[j];
                old[j]=temp;
            }
        }
    }
}