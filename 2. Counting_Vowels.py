
# coding: utf-8

# In[3]:

Vo = "aeiouAEIOU"
Line = input()
vCount, consoCount = 0,0
for i in range(0, len(Line)):
    if Line[i] in Vo:
        vCount += 1
    else:
        consoCount += 1
print(" There are", vCount, "vowels\n", "There are", consoCount, "consonents")

