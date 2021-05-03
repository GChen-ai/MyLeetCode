class Solution {
    public boolean isPalindrome(String s) {
        s=s.toLowerCase();
        int i=0;
        int j=s.length()-1;
        while(i<=j){
            if (s.charAt(i) < '0' || (s.charAt(i) > '9' && s.charAt(i) < 'a') || s.charAt(i) > 'z'){
                i++;
                continue;
            }
            if (s.charAt(j) < '0' || (s.charAt(j) > '9' && s.charAt(j) < 'a') || s.charAt(j) > 'z') {
                j--;
                continue;
            }
            if (s.charAt(i)!=s.charAt(j)) return false;
            i++;
            j--;
        }
        return true;
    }
}