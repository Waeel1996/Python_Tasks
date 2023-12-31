# 1. Check if 10 is bigger than 15 or not
# 2. If 10 is not bigger than15 print x is smaller than 15

x = 10
if x > 15 :
    print ('10 is bigger than 15')
else :
    print ('10 is smaller than 15')

print ('--------------------------------')
# ------------------------------------------------

# 3. In which cases we will use all

print ("we use 'all' if all conditions all true")


print ('--------------------------------')
# ------------------------------------------------

# 4. What is the differences between all , and

print ("we use 'all' if all conditions all true, on the other hand use 'and' if we choosed specific conditions to be checked")


print ('--------------------------------')
# ------------------------------------------------

# 5. What is the differences between any , or

print ("we use 'any' if one of the conditions is true, and we use 'or' if one of specific conditions is true")


print ('--------------------------------')
# ------------------------------------------------

# 6. If we need all the conditions to be true we will use ....

print ("If we need all the conditions to be true we will use : all")


print ('--------------------------------')
# ------------------------------------------------

# 7. What is the differences between if , elif

print ("so the difference is that the code always checks to see if an 'if' statement is true, checks 'elif' statements only if each 'if' and 'elif' statement above it is false")


print ('--------------------------------')
# ------------------------------------------------

# 8. What is the differences between elif else

print ("The elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE, on the other hand, the else keyword decides what to do if the condition is False.")


print ('--------------------------------')
# ------------------------------------------------

# 9. Can we use more than one elif

print ("yes, elif can be used multiple times in one code")


print ('--------------------------------')
# ------------------------------------------------

# 10. Can we use more than one else

print ('No, in Python you cannot use multiple "else" blocks in a row. The "else" condition is typically used after an "if" condition to execute code when none of the previous conditions were met. However, there can only be a single "else" block immediately following the previous block.')


print ('--------------------------------')
# ------------------------------------------------

# 11. write s simple ternary operator

x = 10

print (True) if x >= 10 else print (False)


print ('--------------------------------')
# ------------------------------------------------

# 12. in elif , python will check all the conditions no matter what ?

print('as soon as the condition is true, python will stop checking the other conditions')


print ('--------------------------------')
# ------------------------------------------------

# 13. in elif we use else for ... ?

print ('In Python, the "else" can be used with "elif" statements to handle cases when none of the preceding conditions in the "if"-"elif" chain are satisfied. It provides a default action to be executed if all the previous conditions evaluate to False.')


print ('--------------------------------')
# ------------------------------------------------

# 14. if we have this list [2,4,6,8,10] :

#     1. check to see if 4 in this list or not :

l = [2,4,6,8,10]
if 4 in l :
    print ('the List contains the number 4')
else :
    print ("the List doesn't contain the number 4")

#     2. check to see if 4 and 6 in this list on not :

l = [2,4,6,8,10]
if 4 and 6 in l :
    print ('the List contains the number 4 and 6')
else :
    print ("the List doesn't contain the number 4 and 6")

#     3. check to see if 3 or 6 in this list :

l = [2,4,6,8,10]
if 3 or 6 in l :
    print ('the List contains the number 3 or 6')
else :
    print ("the List doesn't contain the number 3 or 6")

#     4. check to see if 2 , 4 and 5 in this list :

l = [2,4,6,8,10]
if all ([2,4,5]) in l:
    print ('the List contains the numbers 2 , 4 and 5')
else :
    print ("the List doesn't contains the numbers 2 , 4 and 5")


print ('--------------------------------')
# ------------------------------------------------
