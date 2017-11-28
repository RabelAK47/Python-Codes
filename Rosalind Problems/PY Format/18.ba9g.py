
# coding: utf-8

# In[1]:

#Problem: http://rosalind.info/problems/ba9g/

DNA = input()
li = []
dc = {}
for i in range(len(DNA)):
    temp = DNA[i:i+len(DNA)]
    dc[temp] = i
    li.append(temp)
li = sorted(li)
res = ""
for i in range(len(li)):
    temp = li[i]
    if temp in dc:
        res += str(dc[temp]) + ", "
print(res[0: len(res)-2])

