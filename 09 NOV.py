x="Python Programming"
a=x.upper()
print(a)
for i in x:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        print(i,end=",")
print()
i=input()
y=x.replace(i,'')
print(y)