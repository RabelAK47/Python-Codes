
# coding: utf-8

# In[2]:

# Problem http://rosalind.info/problems/ba1d/
A = input()
B = input()
ans = ""
for i in range(len(B)):
    sub = B[i:i+len(A)]
    if sub == A:
        ans = ans + str(i)
        ans += " "
print(ans[0:len(ans)-1])

