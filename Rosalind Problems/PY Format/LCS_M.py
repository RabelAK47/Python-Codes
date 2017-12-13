
# coding: utf-8

# In[ ]:

#BA5C
import numpy as np

str1 = input()
str2 = input()

L = len(str1)
M = len(str2)

arr = np.zeros((L+1, M+1), dtype = np.int)
direction = np.zeros((L+1, M+1), dtype = np.str)

    
for i in range(1, L+1, 1):
    for j in range(1, M+1, 1):
        
        if str1[i-1] == str2[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
            direction[i][j] = 'C'
        
        elif arr[i-1][j] > arr[i][j-1]:
            arr[i][j] = arr[i-1][j]
            direction[i][j] = 'U'
        
        else:
            arr[i][j] = arr[i][j-1]
            direction[i][j] = 'L'

res = ""
while True:
    if L == 0 or M == 0:
        break
    if direction[L][M] == 'C':
        res += str1[L-1]
        L -= 1
        M -= 1
    elif direction[L][M] == 'U':
        L -= 1
    else:
        M -= 1
print(res[::-1])   

# input: AACCTTGG
# input: ACACTGTGA
# output: AACTGG

