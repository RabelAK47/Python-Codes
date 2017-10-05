
# coding: utf-8

# In[31]:

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("All elements:", my_list) # Printing Total List

Len = len(my_list) # Length of a list
print("Length of the List =", Len)

my_list.append(10)  # Adding value to trail
print("New value added in the trail:", my_list)

my_list[2] = 50  # Upadting Index value
print("After upadted Index value:", my_list)

del my_list[6] # Deleting Index Value
print("After upadted Index value:", my_list)

rev = my_list[-1::-1]  # Reversing the List or my_list.reverse()
print("In Reverse:", rev)

my_list.sort()  # List Has been sorted
for i in my_list:
    print(i)

mx = max(my_list) # Max of the List
print("Max of My List is:", mx)

mn = min(my_list) # Min of the List
print("Min of My List is:", mn)

Count = my_list.count(50)
print("Count for", 50, "=", Count)

