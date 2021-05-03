class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result=new ArrayList();
        if (s==null || s.length()==0) return result;
        List<String> path=new ArrayList();
        backtrack(result,path,0,s);
        return result;
    }
    private void backtrack(List<List<String>> result,List<String> path,int cur,String s){
        if (cur>=s.length()){
            result.add(new ArrayList(path));
            return;
        }
        for (int i=cur;i<s.length();i++){
            if (isSubstring(s,cur,i)){
                path.add(s.substring(cur,i+1));
            }else{
                continue;
            }
            backtrack(result,path,i+1,s);
            path.remove(path.size()-1);
        }
    }
    private boolean isSubstring(String s,int start,int end){
        for (int i=start,j=end;i<j;i++,j--){
            if (s.charAt(i)!=s.charAt(j)) return false;
        }
        return true;
    }
}