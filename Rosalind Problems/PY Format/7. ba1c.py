
# coding: utf-8

# In[1]:

# Problem http://rosalind.info/problems/ba1c/
dc = {'A':'T', 'G' : 'C', 'T' : 'A', 'C': 'G'}
st = input()
mystr = ""
for i in st:
    mystr = mystr + dc[i]
print(mystr[::-1])

