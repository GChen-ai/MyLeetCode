class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] result=new int[2];
        if (numbers==null || numbers.length==0 || numbers[0]>target) return result;
        int left=0;
        int right=numbers.length-1;
        while (left<right){
            if (numbers[left]+numbers[right]==target){
                result[0]=left+1;
                result[1]=right+1;
                break;
            }else if (numbers[left]+numbers[right]<target){
                left++;
            }else{
                right--;
            }
        }
        return result;
    }
}