# dict={"a":1,"b":2,"c":2,"d":3,"e":3,"f":4}
# a=[]
# b={}
# for key,val in dict.items():
#     if val not in a:
#         a.append(val)
#         b[key]=val
# print(dict)
# print(b)

# dict1={1:"a",2:"b",2:"c",3:"d"}
# d=frozenset(dict1)
# print(d) 

d={}
print(d)
k=list(input("keys: ").split(","))
v=list(map(int,input("values: ").split(",")))
d=dict(zip(k,v))
print(d)
a=list(input().split(","))
d[a[0]]=int(a[1])
print(d)