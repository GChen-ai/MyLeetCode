class Solution {
    public int trailingZeroes(int n) {
        int result=0;
        int div=5;
        while(div<=n){
            result+=n/div;
            div*=5;
        }
        return result;
    }
}