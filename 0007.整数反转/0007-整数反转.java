class Solution {
    public int reverse(int x) {
        while (x>0 && x%10==0){
            x=x/10;
        }
        int result=0;
        int res=0;
        int mark=1;
        long pre=0;
        if (x<0){
            x=-x;
            mark=-1;
        }
        while (x>0){
            pre=result;
            result=result*10+res;
            if (result>Integer.MAX_VALUE/10) return 0;
            res=x%10;
            x=x/10;
        }
        result=result*10+res;
        return mark*result;
    }
}