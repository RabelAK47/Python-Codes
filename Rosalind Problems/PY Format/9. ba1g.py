
# coding: utf-8

# In[ ]:

# Problem http://rosalind.info/problems/ba1g/
A = input()
B = input()
Count = 0
for i in range(len(A)):
    if A[i] != B[i]:
        Count += 1
print(Count)

