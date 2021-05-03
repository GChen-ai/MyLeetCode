class Solution {
    public void solve(char[][] board) {
        if (board==null || board.length==0 || board[0]==null || board[0].length==0) return;
        for (int i=0;i<board.length;i++){
            for (int j=0;j<board[0].length;j++){
                if (i==0 || j==0 || i==board.length-1 || j==board[0].length-1){
                     if (board[i][j]=='O') dfs(board,i,j);
                }
            }
        }
        
        for (int i=0;i<board.length;i++){
            for (int j=0;j<board[0].length;j++){
                if (board[i][j]=='O') board[i][j]='X';
                if (board[i][j]=='K') board[i][j]='O';
            }
        }
    }
    private void dfs(char[][] board,int x,int y){
        if (x<0 || x>board.length-1 || y<0 || y>board[0].length-1 || board[x][y]=='X' || board[x][y]=='K') return;
        board[x][y]='K';
        dfs(board,x-1,y);
        dfs(board,x+1,y);
        dfs(board,x,y-1);
        dfs(board,x,y+1);
    }
}