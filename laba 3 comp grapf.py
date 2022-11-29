from tkinter import *
from pyautogui import screenshot
from math import pi, cos, sin

def rotate(x, y, teta, center=480):
    ang = (pi/180)*teta
 
    x -= center
    y -= center

    x = x*cos(ang)-y*sin(ang)
    y = y*cos(ang)+x*sin(ang)

    x += center
    y += center

    canvas.create_line(x,y,x+1,y+1, fill="blue")

window_width = 960
window_height = 960

window = Tk()
window.title("Лабораторна робота №3: Афінне перетворення")

canvas = Canvas(window,width=window_width,height=window_height )
w, h = window.winfo_width(), window.winfo_height()
window.geometry("+0+0")
canvas.pack()


file = open("DS3.txt")
for line in file:
    data = line.split(sep=" ")
    x = float(data[0])
    y = float(data[1])
    alpha = 10 * (3 + 1)
    rotate(x, y, alpha)


window.mainloop()
screenshot('screenshot.png', region = (5,30,window_width,window_height+10))
      