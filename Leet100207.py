
def beautifulIndices(s: str, a: str, b: str, k: int):
    def kmp(s,p):
        def build(p):
            nxt = [0]
            pos = 1
            now = 0
            while(pos < len(p)):
                if p[pos] == p[now]:
                    pos += 1
                    now += 1
                    nxt.append(now)
                elif now != 0:
                    now = nxt[now - 1]
                else:
                    nxt.append(0)
                    pos += 1
                # print(nxt)
            return nxt
        
        def search(s,p,nxt):
            l,pos = 0,0
            res = []
            while(l < len(s)):
                if s[l] == p[pos]:
                    l += 1
                    pos += 1
                elif pos!=0:
                    pos = nxt[pos - 1]
                    print(pos)
                else:
                    l += 1

                if pos == len(p):
                    res.append(l - pos)
                    pos = nxt[pos - 1]  
            
            return res
        
        nxt = build(p)
        # return nxt
        return search(s,p,nxt)

    find_i = kmp(s,a)
    find_j = kmp(s,b)
    x = 0
    ans = []
    for val in find_i:
        while x != len(find_j) - 1 and find_j[x] < val:
            x += 1
        if abs(find_j[x] - val) <= k or abs(find_j[x-1] - val) <= k:
            ans.append(val)

    return ans

s = "vatevavakz"
a = "va"
b = "lbda"

print(beautifulIndices(s,a,b,k))