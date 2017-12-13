
# coding: utf-8

# In[19]:

# Problem http://rosalind.info/problems/ba9h/

F = open("C:/Users/Rabel/suff.txt")
DNA = input()
res = ""
li = []
for L in F.readlines():
    temp = L.strip()
    for i in range(len(DNA)):
        sub = DNA[i:i+len(temp)]
        if sub == temp:
            li.append(i)
li = sorted(li)
for i in range(len(li)):
    res += str(li[i]) + " "
print(res)
F.close()

