
# coding: utf-8

# In[1]:

# Problem http://rosalind.info/problems/ba1a/
A = input()
B = input()
Count = 0
for i in range(0, len(A)):
    sub = A[i:i+len(B)]
    if sub == B:
        Count += 1
print(Count)

