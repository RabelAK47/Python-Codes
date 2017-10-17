
# coding: utf-8

# In[18]:

# Problem http://rosalind.info/problems/ba1f/

f = open('G:/Python/Text/input.txt', 'r')
fout = open('G:/Python/Text/output.txt', 'w')

DNA = f.readline()

mn = 9999999999999999
Vec = [0]
Count = 0
for i in range(len(DNA)):
    if Count < mn:
        mn = Count
    if DNA[i] == 'C':
        Count -= 1
    elif DNA[i] == 'G':
        Count += 1
    Vec.append(Count)
ans = ""
for i in range(len(Vec)):
    if mn == Vec[i]:
        ans += str(i) + ' '
fout.write(ans[0:len(ans)-1])
f.close()
fout.close()

