def factorial(n):
    if n==0:
       result=1
    else:
       result=n*factorial(n-1)
    return result
for i in range (11):
    print("the factorial of {}is :{}". format (i, factorial (i)))
