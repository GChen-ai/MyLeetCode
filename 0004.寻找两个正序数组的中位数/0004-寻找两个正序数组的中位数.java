class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int count=(nums1.length+nums2.length)/2+1;
        int n1=0;
        int n2=0;
        float result=0;
        float pre=0;
        while (n1<nums1.length && n2<nums2.length &&count>0){
            if (nums1[n1]<nums2[n2]){
                pre=result;
                result=nums1[n1];
                n1++;
            }else{
                pre=result;
                result=nums2[n2];
                n2++;
            }
            count--;
        }
        while (count>0){
            if (n1>=nums1.length){
                pre=result;
                result=nums2[n2];
                count--;
                n2++;
            }else{
                pre=result;
                result=nums1[n1];
                count--;
                n1++;
            }
        }
        if ((nums1.length+nums2.length)%2==0){
            result=(result+pre)/2;
        }
        return result;
    }
}