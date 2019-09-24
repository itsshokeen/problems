n = int(input())
lt = []
for i in range(n):
    item=int(input())
    lt.append(item)
t = tuple(lt)
print(hash(t))
