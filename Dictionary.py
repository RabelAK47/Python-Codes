
# coding: utf-8

# # Dictionary

# In[90]:

student = {'name': 'Rabel', 'age': 21, 'courses': ['Math', 'Computer Science']}
student['phone'] = '01764553551'
student.update({'phne': '0176455'})
print(student)
print(student.get('name', 'Not Found'))
Age = student.pop('age')
print(Age)
Len = len(student)
print(Len)
K = student.keys()
V = student.values()
I = student.items()
print(K)
print(V)
print(I)

for k in student:
    print(k)
for ke, va in student.items():
    s = str(va) + "AK47"
    student.update({ke:s})
print(student)

