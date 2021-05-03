class Solution {
    public int maxProfit(int[] prices) {
        if (prices==null || prices.length==0) return 0;
        int result=0;
        int min=prices[0];
        for (int i=1;i<prices.length;i++){
            result=(result>prices[i]-min)? result:prices[i]-min;
            min=(prices[i]<min)? prices[i]:min;
        }
        return result;
    }
}