from tkinter import *
from random import randint
characters = [i for i in range(49, 58)]+[i for i in range(65, 91)]
def key():
    return(f"{randint(0,10)}{randint(0,10)}{randint(0,10)}{randint(0,10)}{randint(0,10)}")
def block():
    
#setting up the window
# window = Tk()
# window.geometry('576x360')
# bg_img = PhotoImage(file='cursedminecraft.png')

# lbl_bg = Label(window, image=bg_img)
# lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)



# window.mainloop()
# from random import randint
print(f"{key()}-{key()}")
print([chr(i) for i in characters])
# print(sum(characters)/len(characters))  71.2  71.2*5=356 so acceptable interval seems to be [300, 400]
