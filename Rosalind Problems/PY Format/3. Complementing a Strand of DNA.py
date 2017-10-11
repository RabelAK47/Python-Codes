
# coding: utf-8

# In[1]:

# Problem http://rosalind.info/problems/revc/.
Mp = {'A':'T', 'C':'G', 'G': 'C', 'T':'A'}
DNA = input()
Rev = ""
for i in range(len(DNA)):
    Rev += Mp[DNA[i]]
print(Rev[::-1])

