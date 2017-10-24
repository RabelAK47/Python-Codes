
# coding: utf-8

# In[6]:

'''
Problem: http://rosalind.info/problems/prot/ 
'''

F = open('C:/Users/Rabel/DC_Input.txt', 'r')
S = open('C:/Users/Rabel/rosalind_prot.txt', 'r')
Fout = open('C:/Users/Rabel/My_Output.txt', 'w')
dc = {}
for L in F.readlines():
    temp = L.strip()
    key = temp[0:3]
    val = temp[4:4+len(temp)]
    dc[key] = val
DNA = S.readline().strip()
DNA = DNA.replace('T', 'U')
ans = ""
for i in range(0, len(DNA), 3):
    sub = DNA[i:i+3]
    if sub in dc:
        temp = dc[sub]
        if temp == "Stop":
            break
        else:
            ans += temp
Fout.write(ans)
F.close()
S.close()
Fout.close()

