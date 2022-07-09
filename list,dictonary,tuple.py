l=[]
l.append(5)
l.append(10)
print("adding one element from list",l)
l.pop()
print("popped one element from list",l)
print()
t=tuple(l)
print("tuple",t)
print()
d={}
d[5]="five"
d[10]="ten"
print("dictonary",d)
del d[10]
print("dictonary",d)