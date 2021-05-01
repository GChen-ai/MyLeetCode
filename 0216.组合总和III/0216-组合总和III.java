class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result=new ArrayList();
        List<Integer> path=new ArrayList();
        backtrack(k,n,1,result,path);
        return result;
    }
    private void backtrack(int k,int n,int cur,List<List<Integer>> result,List<Integer> path){
        if (k==0 && n==0){
            result.add(new ArrayList(path));
            return;
        }
        if (k<0 || n<0) return;
        for (int i=cur;i<10;i++){
            path.add(i);
            backtrack(k-1,n-i,i+1,result,path);
            path.remove(path.size()-1);
        }
        return;
    }
}