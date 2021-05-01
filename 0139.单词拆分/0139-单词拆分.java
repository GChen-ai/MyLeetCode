class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        if (s==null || s.length()==0 || wordDict==null || wordDict.size()==0) return false;
        boolean[] mem=new boolean[s.length()];
        HashSet<String> set=new HashSet(wordDict);
        return backtrack(s,set,0,mem);

    }
    private boolean backtrack(String s,HashSet<String> set,int cur,boolean[] mem){
        boolean result=false;
        if (cur>=s.length()){
            result=true;
            return result;
        }
        if (mem[cur]) return false;
        for (int i=cur;i<s.length();i++){
            if (!set.contains(s.substring(cur,i+1))){
                continue;
            }
            result=backtrack(s,set,i+1,mem);
            if (result) return result;;
        }
        mem[cur]=true;
        return result;
    }
}