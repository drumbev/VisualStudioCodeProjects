# y = x^0.5
m, n = 22, 9
graph = [[0 for i in range(n)] for i in range(m)]

# # for i in graph:
    










#вывод графика с значениями х и у
for i in range(1, m):
    
    print((m-i)*3 + 33,' ', '   '.join(map(str, graph[i])))
    
print('     .' + '   .'*8)
print('     ',end = '')
for j in range(n):
    print(f'{j+1}K ', end = ' ')
print(end = '\n')
    
#оценка нужных значений
a = []
for i in range(1, 10):
    y = (10-i)*1000
    x = y **0.5
    if abs(x - (x//3)*3)<=1.5:
        x = x//3*3
    else:
        x = x//3*3 + 3
    print(y, x)
