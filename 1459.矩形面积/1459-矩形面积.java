class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int top=Math.min(D,H);
        int left=Math.max(A,E);
        int bottom=Math.max(B,F);
        int right=Math.min(C,G);

        int sumAll=(C-A)*(D-B)+(G-E)*(H-F);
        if (E>=C || G<=A || B>=H || F>=D) return sumAll;
        return sumAll-Math.abs(top-bottom)*Math.abs(right-left);
    }
}