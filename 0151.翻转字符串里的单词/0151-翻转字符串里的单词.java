class Solution {
    public String reverseWords(String s) {
        if (s==null || s.length()==0) return null;
        String[] str = s.split(" ");
        StringBuilder result = new StringBuilder();
        for (int i=str.length-1;i>=0;i--){
            if (str[i]==null || str[i].length()==0) continue;
            result.append(str[i]+" ");
            
        }
        return result.toString().trim();
    }
}