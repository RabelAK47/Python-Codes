
# coding: utf-8

# In[1]:

# Task-4: Complement: Find the complement of a DNA string
# -------------input: TGCTAC output: ACGATG ---------------------

com = input()
after_com = ""
for i in range(len(com)):
    if com[i] == 'T':
        after_com += 'A'
    elif com[i] == 'G':
        after_com += 'C'
    elif com[i] == 'A':
        after_com += 'T'
    elif com[i] == 'C':
        after_com += 'G'
    else:
        after_com += com[i]
print(after_com)

