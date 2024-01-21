from tkinter import *
from random import randint
characters = [i for i in range(49, 58)]+[i for i in range(65, 91)]

#setting up functions
def block():
    sum = 0
    blok = ""
    while sum < 250 or sum > 400:
        blok = f"{chr(characters[randint(0, len(characters)-1)])}{chr(characters[randint(0, len(characters)-1)])}{chr(characters[randint(0, len(characters)-1)])}{chr(characters[randint(0, len(characters)-1)])}"
        sum = 0
        for i in blok:
          sum+=ord(i)
    return blok

def clicked():
    key_lbl.configure(text=f"{block()}-{block()}-{block()}")
    
#setting up the window
window = Tk()
window.geometry('576x360')

bg_img = PhotoImage(file='cursedminecraft.png')
lbl_bg = Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

key_lbl= Label(frame, text = "XXXX-XXXX-XXXX")
key_lbl.grid(column=0, row=20)



btn = Button(frame, text = "generate unique key", command=clicked)
btn.grid(column=0, row=0)



window.mainloop()



## determining the intreval               
# print([chr(i) for i in characters])
# print(sum(characters)/len(characters))  71.2  71.2*4=284.8 so acceptable interval seems to be [250, 400]

# #checking if the blok's weight is correct
# s = "Y3CC"
# c=0
# for i in s:
#     c+=ord(i)
# print(c)

