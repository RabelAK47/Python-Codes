
# coding: utf-8

# In[1]:

# Task1:  Count the number of vowels in a text.
VO = "aeiouAEIOU"
Count = 0
st = input()
for i in st:
    if i in VO:
        Count = Count + 1
print(Count)

