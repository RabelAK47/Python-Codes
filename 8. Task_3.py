
# coding: utf-8

# In[4]:

# Task3: Count the number of each nucleotide in a DNA string
# -----------------input: ACCGACTTTT output: 2, 3, 1, 4 -----------------------¶

nuec = input()
a, c, g, t = 0,0,0,0
for i in range(len(nuec)):
    if nuec[i] == 'A':
        a += 1
    elif nuec[i] == 'C':
        c += 1
    elif nuec[i] == 'G':
        g += 1
    elif nuec[i] == 'T':
        t += 1
print("A=", a, "C=", c, "G=", g, "T=",t)

