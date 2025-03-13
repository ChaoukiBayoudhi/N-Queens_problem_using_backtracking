import random as r
n=10
L=[r.randint(1,100) for _ in range(n)]
print(L)
for index,content in enumerate(L):
    print(index,content)

res=[(index,content) for index,content in enumerate(L)]
print(res[3][1])