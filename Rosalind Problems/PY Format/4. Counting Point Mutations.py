
# coding: utf-8

# In[1]:

# Problem http://rosalind.info/problems/hamm/
S = input()
T = input()
Count = 0
for i in range(len(S)):
    if S[i] != T[i]:
        Count += 1
print(Count)

