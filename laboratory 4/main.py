# # 3x3, no illness, 15 survival points
# stuffdict= {"r":(3, 25), "p":(2, 15), "a":(2, 15), "m":(2, 20), "i":(1, 5), "k":(1, 15), "x":(3, 20), "t":(1, 25), "f":(1, 15), "d":(1, 20), "s":(2, 20), "c":(2, 20)}
# mass = [3, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 2]
# points = [25, 15, 15, 20, 5, 15, 20, 25, 15, 20, 20, 20]
# N=12 # количество предметов
# S=9 # вместимость по "весу"
# # print(get_mass_and_points("r"))

# matrix = [["0" for i in range(S+1)] for j in range(N+1)]
# for i in range(1, N):
#     for j in range(1, S):
#         matrix[i][j] = 
        
    



# for i in matrix:
#     print("  ".join(map(str, i)))
# print(len(mass), len(points))
class Item:
    def __init__(self, name, symbol, size, value):
        self.name = name
        self.symbol = symbol
        self.size = size
        self.value = value

def bag(items, capacity):
    n = len(items)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if items[i - 1].size > w:
                table[i][w] = table[i - 1][w]
            else:
                table[i][w] = max(table[i - 1][w], table[i - 1][w - items[i - 1].size] + items[i - 1].value)

    result = []
    w = capacity
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
            result.append(items[i - 1])
            w -= items[i - 1].size

    return result

items = [Item("Винтовка", "r", 3, 25), Item("Пистолет", "p", 2, 15), Item("Боекомплект", "a", 2, 15), Item("Аптечка", "m", 2, 20), Item("Ингалятор", "i", 1, 5), Item("Нож", "k", 1, 15), Item("Топор", "x", 3, 20), Item("Оберег", "t", 1, 25), Item("Фляжка", "f", 1, 15), Item("Антидот", "d", 1, 10), Item("Еда", "s", 2, 20), Item("Арбалет", "c", 2, 20)]

capacity = 15
selected_items = bag(items, capacity)
for item in selected_items:
    print(item.symbol, end = ' ')
    


