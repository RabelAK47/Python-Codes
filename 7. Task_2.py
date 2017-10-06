
# coding: utf-8

# In[2]:

# Task2: GC percentage: Cunt the total percentage of G+C nucleotides in a DNA sequence
myst = input()
ans = 0
Len = len(myst)
for i in myst:
    if i in "GC":
        ans = ans + 1
temp = ans * 100
res = temp / Len
print(res, "%")

