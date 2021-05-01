class Solution {
    public int minSwapsCouples(int[] row) {
        Map<Integer,Integer> map=new HashMap();
        int count=0;
        for (int i=0;i<row.length;i++){
            map.put(row[i],i);
        }
        int temp=0;
        int index=0;
        for (int i=0;i<row.length;i+=2){
            if ((row[i]%2==0 && row[i]-row[i+1]!=-1) || (row[i]%2==1 && row[i]-row[i+1]!=1)){
                temp=row[i+1];
                if (row[i]%2==0){
                    row[i+1]=row[i]+1;
                    index=map.get(row[i]+1);
                    row[index]=temp;
                    map.put(temp,index);
                }else{
                    row[i+1]=row[i]-1;
                    index=map.get(row[i]-1);
                    row[index]=temp;
                    map.put(temp,index);
                }
                count+=1;
            }

        }
        return count;
    }
}