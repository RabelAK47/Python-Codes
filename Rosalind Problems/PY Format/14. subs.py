
# coding: utf-8

# In[16]:

'''
http://rosalind.info/problems/subs/
'''

A = input()
B = input()
ans = ""
for i in range(len(A)):
    sub = A[i:i+len(B)]
    if sub == B:
        ans += str(i+1) + " "
print(ans[0:len(ans)-1])

