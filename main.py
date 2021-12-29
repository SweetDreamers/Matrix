from tkinter import *
import random
import time

root = Tk()
root.title('Матрица')
root.geometry('700x700+300+300')
root.resizable(width=False, height=False)

c = Canvas(root, width=700, height=700, bg='black')
c.pack()

alphabet = 'qwertyuiop[]{}asdfghjkl;zxcvbnm<>?/|'
alphabet.split()
print(alphabet)
print(len(alphabet))
h = 0

while True:
    c.delete('t' + str(h))
    for i in range(1, 35):
        r = random.randint(0, 35)
        ct = c.create_text(20 * i, h, text=str(alphabet[r]), fill='lime', font=('Comic Sans MS', 11), tag='t' + str(h))
        rdm = random.randint(1, 10)
        for j in range(10):
            c.move(ct, 0, rdm)
    c.update()
    h += 20
    if h >= 650:
        h = 0


