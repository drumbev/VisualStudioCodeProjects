# y = x^0.5
m, n = 22, 9
graph = [[0 for i in range(n)] for i in range(m)]

#оценка нужных значений
a = []
for i in range(1, 10):
    y = (10-i)*1000
    x = y **0.5
    if abs(x - (x//3)*3)<=1.5:
        x = int(x//3*3)
    else:
        x = int(x//3*3 + 3)
    print(y, x)


#заполнение значений
for i in range(m):
    for j in range(n):
        x = (j+1)*1000
        y = x **0.5
        if abs(y - (y//3)*3)<=1.5:
            y = int(y//3*3)
        else:
            y = int(y//3*3 + 3)  
        if y == (m-i)*3 + 30:
            graph[i][j] = '+'








#вывод графика с значениями х и у
for i in range(m):    
    print((m-i)*3 + 30,' ', '   '.join(map(str, graph[i])))



   
print('     .' + '   .'*8)
print('     ',end = '')
for j in range(n):
    print(f'{j+1}K ', end = ' ')
print(end = '\n')
    
