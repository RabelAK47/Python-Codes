
# coding: utf-8

# In[5]:

st = input()
total = 0
rev = st[::-1]
for i in range(len(rev)):
    temp = int(rev[i]) * (4**i)
    total += temp
print(st, "in decimal:", total)

