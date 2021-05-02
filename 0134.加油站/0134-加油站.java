class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int loc=0;
        int left=0;
        int gasSum=0;
        int costSum=0;
        for (int i=0;i<gas.length;i++){
            gasSum+=gas[i];
            costSum+=cost[i];
            left+=gas[i]-cost[i];
            if (left<0){
                loc=i+1;
                left=0;
            }
        }
        if (gasSum<costSum) return -1;
        return loc;
            
    }
}