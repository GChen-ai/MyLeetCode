class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> result=new ArrayList();
        List<Integer> pre=new ArrayList();
        for (int i=0;i<=rowIndex;i++){
            List<Integer> temp=new ArrayList();
            for (int j=0;j<=i;j++){
                if (j==0 || j==i){
                    temp.add(1);
                }else{
                    temp.add(pre.get(j)+pre.get(j-1));
                }
            }
            pre=temp;
            result=temp;
        }
        return result;
    }
}