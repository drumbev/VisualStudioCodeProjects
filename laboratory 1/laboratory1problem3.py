# y = x^0.5
# graph = [[0 for i in range(10)] for i in range(12)]

# # for i in graph:
    











# for i in graph:
#     print(' '.join(map(str, i)))
a = []
b = []
for i in range(10):
    y = (10-i)*1000
    x = y **0.5
    if abs(x - (x//3)*3)<=1.5:
        x = x//3*3
    else:
        x = x//3*3 + 3
    print(y, y **0.5, x/3)
    a.append(y**0.5)
for i  in  range(len(a) -1):
    b.append(a[i]-a[i+1])
print(b)
    