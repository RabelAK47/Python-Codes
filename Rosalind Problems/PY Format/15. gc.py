
# coding: utf-8

# In[51]:

'''
http://rosalind.info/problems/gc/
'''

from Bio import SeqIO
path = 'C:/Users/Rabel/my_data.fasta'
records = list(SeqIO.parse(path, "fasta"))
dc = {}
mx = -99999999999.9
for i in range(len(records)):
    ID = records[i].id
    DNA = records[i].seq
    Count = 0
    total = len(DNA)
    for j in DNA:
        if j in "GC":
            Count += 1
    temp = 100* float(Count)/total
    dc[ID] = temp
    if temp > mx:
        mx = temp
for key, val in dc.items():
    if val == mx:
        print(key)
        print("%.6f" % val)
        break

