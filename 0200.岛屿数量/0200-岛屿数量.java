class Solution {
    public int numIslands(char[][] grid) {
        if (grid==null || grid.length==0) return 0;
        int num=0;
        for (int i=0;i<grid.length;i++){
            for (int j=0;j<grid[0].length;j++){
                if (grid[i][j]=='1'){
                    dfs(grid,i,j);
                    num++;
                }
            }
        }
        return num;
    }
    private void dfs(char[][] grid,int x, int y){
        if (grid[x][y]!='1') return;
        grid[x][y]='2';
        if (x+1<=grid.length-1) dfs(grid,x+1,y);
        if (x-1>=0) dfs(grid,x-1,y);
        if (y+1<=grid[0].length-1) dfs(grid,x,y+1);
        if (y-1>=0) dfs(grid,x,y-1);
        return;
    }
}