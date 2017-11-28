
# coding: utf-8

# In[29]:

#Problem: http://rosalind.info/problems/ba9q/

def suff(text, K):
    my_list = []
    dc = {}
    for i in range(len(text)):
        sub = text[i:]
        my_list.append(sub)
        dc[sub] = i
    my_list.sort()
    for i in range(len(my_list)):
        temp = my_list[i]
        if temp in dc and dc[temp]%K == 0:
            ans = str(i) + "," + str(dc[temp])
            print(ans)
text = input()
K = int(input())
suff(text, K)

