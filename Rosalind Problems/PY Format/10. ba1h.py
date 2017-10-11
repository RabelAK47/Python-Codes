
# coding: utf-8

# In[1]:

# Problem http://rosalind.info/problems/ba1h/
A = input()
B = input()
K = int(input())
ans = ""
for i in range(len(B)):
    sub = B[i: i+len(A)]
    if len(sub) == len(A):
        Count = 0
        for j in range(len(A)):
            if A[j] != sub[j] :
                Count += 1
        if Count <= K:
            ans = ans + str(i)
            ans = ans + ' '
print(ans[0:len(ans)-1])

