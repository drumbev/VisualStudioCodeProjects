# y = x^0.5
m, n = 22, 10
graph = [[0 for i in range(m)] for i in range(n)]

# # for i in graph:
    










#вывод графика с значениями х и у
for i in range(1, len(graph)):
    
    print((n-i)*1000, ' . ','  '.join(map(str, graph[i])))
print('     ', end = '')
for j in range(1, 22):
    print(j*3 + 33, end = ' ')
print(end = '\n')
    
#оценка нужных значений
a = []
b = []
for i in range(10):
    y = (10-i)*1000
    x = y **0.5
    if abs(x - (x//3)*3)<=1.5:
        x = x//3*3
    else:
        x = x//3*3 + 3
    print(y, y **0.5, x, x/3)
    a.append(y**0.5)
for i  in  range(len(a) -1):
    b.append(a[i]-a[i+1])
print(b)
    