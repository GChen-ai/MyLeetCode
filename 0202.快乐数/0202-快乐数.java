class Solution {
    public boolean isHappy(int n) {
        int result=0;
        int slow=n;
        int fast=change(n);
        while(slow!=fast){
            slow=change(slow);
            fast=change(change(fast));
            if (slow==1) return true;
        }
        return slow==1;
    }
    private int change(int n){
        int result=0;
        int res=0;
        while (n>0){
            res=n%10;
            n/=10;
            result+=res*res;
        }
        return result;
    }
}