class Solution:
    def minimumEffortPath(self, heights) -> int:
        n = len(heights)
        m = len(heights[0])
        dicr = [(0,1),(1,0),(0,-1),(-1,0)]
        l,r,mid = 0,1000000,0
        def check(k):
            vis = [[False for _ in range(m)] for __ in range(n)]

            def dfs(x,y,k):
                vis[x][y] = True
                
                if x == n - 1 and y == m - 1:
                    return True
                
                for dx,dy in dicr:
                    nx = x + dx
                    ny = y + dy
                    # print(vis[0][1])
                    if nx < n and ny < m and nx >= 0 and ny >= 0 and abs(heights[x][y] - heights[nx][ny]) <= k and vis[nx][ny] == False:
                        vis[nx][ny] = True
                        print(nx,ny,vis[nx][ny])
                        if dfs(nx,ny,k) == True:
                            return True
                
                return False
            
            return dfs(0,0,k)
        # return check(0)
        while(l<=r):
            mid = (l+r) >> 1
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return mid

if __name__ == "__main__":
    x = Solution()
    # print()
    height = [[1,2,2],[3,8,2],[5,3,5]]
    # print(height[0][1])
    print(x.minimumEffortPath(height))