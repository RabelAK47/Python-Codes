
# coding: utf-8

# In[1]:

# Task-5: Reverse Complement: Find the reverse complent of a DNA string¶
# ------------------input: TGCTAC output: GTAGCA ----------------------

DNA = input()
rev = ""
for i in range(len(DNA)):
    if DNA[i] == 'T':
        rev += 'A'
    elif DNA[i] == 'G':
        rev += 'C'
    elif DNA[i] == 'A':
        rev += 'T'
    elif DNA[i] == 'C':
        rev += 'G'
    else:
        rev += DNA[i]
print(rev[::-1])

