class Solution:
    #思路：转换题意，从凑amount变成将amount减成0
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = 1 << amount
        # 创建dp数组，第i位是1代表可以减到i，0代表不能
        result = 0
        #减少的次数
        while dp & 1 == 0:
            #若第0位为0则说明amount能取到
            t = dp
            for coin in coins:
                dp |= t >> coin
                #右移操作 == 减操作
                #右移dp数组代表同时更新之前的1状态
                #等价与for i in range(amount): dp[i] |= dp[i-coin]
            if dp == t:
                return -1
            #如果做不了任何操作就代表不可能实现
            result += 1
            #操作次数加1
        return result