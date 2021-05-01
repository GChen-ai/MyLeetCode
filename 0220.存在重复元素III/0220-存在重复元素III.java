class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        Map<Long,Long> b=new HashMap();
        long cur=0;
        long w=(long)t+1;
        for (int i=0;i<nums.length;i++){
            cur=div((long)nums[i],w);
            if (b.containsKey(cur)) return true;
            b.put(cur,(long)nums[i]);
            if (b.containsKey(cur-1) && Math.abs(b.get(cur-1)-nums[i])<w) return true;
            if (b.containsKey(cur+1) && Math.abs(b.get(cur+1)-nums[i])<w) return true;
            if (i>=k) b.remove(nums[i-k]/w);
        }
        return false;
    }
    private long div(long n1,long n2){
        return (n1<0)?(n1+1)/n2-1:n1/n2;
    }
}