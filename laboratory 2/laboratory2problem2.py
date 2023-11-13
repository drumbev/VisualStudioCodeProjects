# The physical body exists at a less evolved plane only to verify one’s existence in the universe.
# aut = input('type authors name ').lower()
file = open('books-en.csv')
s = file.readline()
for i in file:
    author = i.split(';')[2].lower()
    price = i.split(';')[-1]
    # book = i.split(';')[1]
    # condition = aut in author or all(i in author.split(' ') for i in aut.split(' '))  
    # print(i)
    # if condition:
    #     if int(price[:-2]) > 200:
    #         print(f"the book {book} is too expensive")
    #     else:
    #         print(f'your book is {book} by {author} and it costs {price} Rubbles')
    print(int(price[:-1]))


# пояснение к части условия после all    
# a = {1, 3, 4, 4, 5, 6, 2, 6}
# b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# c = [i in b for i in a]
# cond = all(c)
# print(cond)
