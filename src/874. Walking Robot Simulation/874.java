class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
            int[][] directions = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };
            int x = 0, y=0;
            int di=0;
            int ans = 0;
            Set<String> obstacleSet = new HashSet<String>();
            for (int i=0;i<obstacles.length;i++) {
                obstacleSet.add(obstacles[i][0]+","+obstacles[i][1]);
            }
            
            for (int i=0;i<commands.length;i++) {
                if (commands[i]==-1) {
                    di=(di+1)%4;
                }else if (commands[i]==-2) {
                    di=(di+3)%4;
                }
                else if (commands[i]>0) {
                    for (int j=1;j<=commands[i];j++) {
                        int next_x = x+ directions[di][0];
                        int next_y = y+ directions[di][1];
                        if (obstacleSet.contains(next_x+","+next_y)) {
                            break;
                        }else {
                            x = next_x;
                            y = next_y;
                            ans = Math.max(ans, x*x+y*y);
                        }
                    }
                }
            }
            return ans;
        }

}