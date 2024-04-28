class Solution:
    def less(self, a, b):
        
        if a[0]<b[0] or a[1]<b[1]:
            return True
       
        return False
    
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort()
        N = len(envelopes)
        dp = []
        ans = 0 
        check = []
        for envelope in envelopes:
            l = 0
            r = len(dp) - 1
            while(l<=r):
                mid = (l+r) // 2
                if(self.less(envelope, dp[mid])):
                    # check.append(dp[mid])
                    l = mid + 1
                else:
                    r = mid - 1
            print(l,r,(l+r)//2)
            if l >= len(dp):
                dp.append(envelope)
            else:
                dp[l] = envelope
            
            check.append(dp)
        
        return check
    
a = Solution()
print(a.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))