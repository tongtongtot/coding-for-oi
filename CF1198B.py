class Solution:
    def __init__(self):
        pass
    def Welfare(self, n, a, nq, q):
        suf = [-1000000000] * (nq+1)
        pos = [0] * n
        for i in range(nq-1,-1,-1):
            if len(q[i]) == 2:
                suf[i] = max(suf[i+1],q[i][1])
            else:
                suf[i] = suf[i+1]
        
        for i,x in enumerate(q):
            if x[0] == 1:
                a[x[1]-1] = x[2]
                pos[x[1]-1] = i
        
        for i in range(n):
            a[i] = max(a[i],suf[pos[i]])
        # print(suf)
        # print(a)
        for x in a:
            print(x, end=' ')
        

n = int (input())
a = list(map(int, input().split()))
nq = int (input())
q = []
# print(n)
for i in range(nq):
    tmp = list(map(int, input().split()))
    q.append(tmp)
S = Solution()
S.Welfare(n,a,nq,q)
# b = list (map (int, input ). split 0))