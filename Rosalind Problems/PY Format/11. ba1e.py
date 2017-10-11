
# coding: utf-8

# In[ ]:

# Problem http://rosalind.info/problems/ba1e/
def Mapping(G, K):
    mp = {}
    for i in range(len(G)):
        sub = G[i:i+K]
        if len(sub) == K:
            if sub not in mp:
                mp[sub] = 1
            else:
                mp[sub] += 1
    return mp

def Clumps(Mp, G, L, T):
    ans = ""
    visit = {}
    for key, val in Mp.items():
        if val >= T:
            for i in range(len(G)):
                sub2 = G[i: i+L]
                if len(sub2) == L and sub2.count(key) >= T and key not in visit:
                    ans += key+" "
                    visit[key] = key
    return ans[:len(ans)-1]

G = input()
K = int(input())
L = int(input())
T = int(input())

Mp = Mapping(G, K)
res = Clumps(Mp, G, L, T)
print(res)

