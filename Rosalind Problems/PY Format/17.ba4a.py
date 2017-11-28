
# coding: utf-8

# In[ ]:

#Problem: http://rosalind.info/problems/ba4a/

F = open('D:/Rabel/DC_Input.txt', 'r')
S = open('D:/Rabel/rosalind_prot.txt', 'r')
Fout = open('D:/Rabel/My_Output.txt', 'w')
dc = {}
for L in F.readlines():
    temp = L.strip()
    key = temp[0:3]
    val = temp[4:4+len(temp)]
    dc[key] = val
    
DNA = S.readline().strip()
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

