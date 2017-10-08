
# coding: utf-8

# In[23]:

dc = {}
st = input()
K = int(input())
mx = -99999999
for i in range(0, len(st)):
    sub = st[i:i+K]
    if len(sub) == K:
        check = dc.get(sub, 'NotFound')
        if check == 'NotFound':
            dc[sub] = 0
        dc[sub] = dc[sub] + 1
        if dc[sub] > mx:
            mx = dc[sub]
for ke, va in dc.items():
    if va == mx:
        print(ke, va)

