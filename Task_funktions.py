# 1. Create a simple function that takes 2 numbers and print their values :

def func(x,y):
    print(x,y)
func(1,2)



print ('--------------------------------')
# ------------------------------------------------

#2. Create a simple function that takes 2 numbers and return their values

def func1(x,y):
    return x,y
f1=func1(2,3)
print ('f1 =',(f1))



print ('--------------------------------')
# ------------------------------------------------

# 3. In the above return function , use keyword arguments when calling the function


def func1(x,y):
    return x,y
f1=func1(x=2,y=3)
print ('f1 =',(f1))



print ('--------------------------------')
# ------------------------------------------------

# 4. In the above return function , give x and y default values of 0 and call the function with no arguments

def func1(x=0,y=0):
    return x,y
f1=func1()
print ('f1 =',(f1))



print ('--------------------------------')
# ------------------------------------------------

# 5. Create a function that can take any number of arguments and print the sum of them

def func1(x,y):
    return x+y
f1=func1(2,3)
print ('f1 =',(f1))



print ('--------------------------------')
# ------------------------------------------------

# 6. Create the same sum function using the lambda

func1 = lambda x,y : x+y
print (func1(1,2))



print ('--------------------------------')
# ------------------------------------------------

# 7. Call the lambda function at the same definition line

func1 = lambda x,y : x+y; print (func1(1,2))



print ('--------------------------------')
# ------------------------------------------------
