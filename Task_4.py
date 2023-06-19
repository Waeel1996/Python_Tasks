# 1. Print numbers from 0 to 10 using while

x = 0
while x<=10 :
    print (x)
    x+=1


print ('--------------------------------')
# ------------------------------------------------

# 2. Print numbers from 0 to 1o using for

x = 0
for x in range (11):
    print (x)
    x+=1
    

print ('--------------------------------')
# ------------------------------------------------

# 3. Stop the loop if the number = 5

x = 0
for x in range (11):
    print (x)
    if x == 5:
        break
    

print ('--------------------------------')
# ------------------------------------------------

#4. Skip the 5 iteration from print

x = 0
for x in range (11):
    if x == 5:
        continue
    print (x)

print ('--------------------------------')
# ------------------------------------------------
