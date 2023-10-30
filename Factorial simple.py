#simple factorial in my own thinking
n=int(input("Enter a number:"))
lists=[]
for i in range(1,n+1):
    lists.append(i)
mul=1
for i in lists:
   mul= i*mul
    
print("The factorial of a number {} is {}".format(n,mul))
