#No matter where you go, everyone's connected
file = open('books-en.csv')
count = 0
for i in file:
    book_title = (i.split(';'))[1]
    if len(book_title)>30:
        print(book_title)
        count+=1
print(count)
