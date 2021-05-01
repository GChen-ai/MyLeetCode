class Solution {
    public int maxArea(int[] height) {
        int l=0;
        int r=height.length-1;
        int result=0;
        while (l<r){
            result=Math.max(result,(r-l)*Math.min(height[r],height[l]));
            if (height[r]>height[l]){
                l++;
            }else{
                r--;
            }
        }
        return result;
    }
}