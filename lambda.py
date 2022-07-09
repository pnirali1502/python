d=lambda p:p*5
t=lambda p:p*2
x=7
x=d(x)
x=t(x)
x=d(x)
print(x)
nums=[6,16,26,36,46,56]
result=list(map(lambda x:x*2+2-4,nums))
print(result)
t=[1,2,3,4,5,6,7,8,9]
result=filter(lambda v:v%2!=0,t)
print(list(result))