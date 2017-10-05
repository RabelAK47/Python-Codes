
# coding: utf-8

# In[11]:

def CGPA(total):
    if total >= 80 and total <= 100 :
        return "A+"
    elif total >= 75 and total < 80 :
        return "A"
    elif total >= 70 and total < 75 :
        return "A-"
    elif total >= 65 and total < 70 :
        return "B+"
    elif total >= 60 and total < 65 :
        return "B"
    elif total >= 55 and total < 60 :
        return "B-"
    elif total >= 50 and total < 55 :
        return "C+"
    elif total >= 45 and total < 50 :
        return "C"
    elif total >= 40 and total < 45 :
        return "D"

def check_sixty(N):
    if N < 0 or N > 60 :
        return False
    return True

def check_fourty(N):
    if N < 0 or N > 40 :
        return False
    return True

def pass_both(Sixty, Fourty):
    if Sixty >= 24 and Sixty <= 60 and Fourty >= 16 and Fourty <= 40 :
        return True
    return False
    
sixty_marks = float(input("Enter sixty marks: "))
fourty_marks = float(input("Enter fourty marks: "))

if check_sixty(sixty_marks) == False :
    print("Invalid in Sixty Marks input")
    
if check_fourty(fourty_marks) == False :
    print("Invalid in Fourty Marks input")
    
if sixty_marks < 24 and check_sixty(sixty_marks) == True and check_fourty(fourty_marks) == True : 
    print("Failed(R) You can not sit in the final exam!!!")
    
if sixty_marks >= 24 and fourty_marks < 16 and check_fourty(fourty_marks) == True :
    print("Failed(S)")

if pass_both(sixty_marks, fourty_marks) == True :
    total = sixty_marks + fourty_marks
    print(CGPA(total))

