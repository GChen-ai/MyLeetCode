class Solution {
    public int maxProfit(int[] prices) {
        if (prices==null || prices.length==0) return 0;
        int buyFirst=prices[0];
        int buySecond=prices[0];
        int profitFirst=0;
        int profitSecond=0;
        for (int i=0;i<prices.length;i++){
            buyFirst=Math.min(buyFirst,prices[i]);
            profitFirst=Math.max(profitFirst,prices[i]-buyFirst);
            buySecond=Math.min(buySecond,prices[i]-profitFirst);
            profitSecond=Math.max(profitSecond,prices[i]-buySecond);
        }
        return profitSecond;
    }
}