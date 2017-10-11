
# coding: utf-8

# In[ ]:

# Problem http://rosalind.info/problems/ba1b/
st = input()
K = int(input())
dc = {}
mx = -999999999999999
for i in range(len(st)):
    sub = st[i:i+K]
    if sub not in dc:
        dc[sub] = 1
    else:
        dc[sub] += 1
    if dc[sub] > mx:
        mx = dc[sub]
ans = ""
for key, val in dc.items():
    if val == mx:
        ans += key
        ans += " "
print(ans[0:len(ans)-1])

