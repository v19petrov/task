import time
from tkinter import *


class Trafficlight:

    def running(self):
        root = Tk()
        red = Frame(root, width=100, height=100, bg="red")
        time.sleep(1)

        yellow = Frame(root, width=100, height=100, bg="yellow")
        time.sleep(2)

        green = Frame(root, width=100, height=100, bg="green")
        time.sleep(3)

        red.pack()
        yellow.pack()
        green.pack()
        root.mainloop()


t = Trafficlight()
t.running()
