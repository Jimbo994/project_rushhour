
import math
import time

from Tkinter import *
import Tkinter as visual
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

# # stackoverflow.com/questions/38676617/tkinter-show-splash-screen-and-hide-main-screen-until-init-has-finished
# class Instructions(visual.Toplevel):
#     def __init__(self, parent):
#         visual.Toplevel.__init__(self, parent)
#         self.title("Instructions")
#         # some instructions that'll appear on screen
#         self.update()

class BoardVisualization(visual.Tk):
    def __init__(self, width, height):
        "Initializes a visualization with the specified parameters."

        self.max_dim = max(width, height)
        self.width = width
        self.height = height

        visual.Tk.__init__(self)
        self.withdraw()
        instruction = Instructions(self)
    # self.title("Main Window")
        time.sleep(3)
        instruction.destroy()

        # self.vehicles = vehicles

        # Initialize a drawing surface
        self.master = Tk()
        self.title("RUSH HOUR")
        self.w = Canvas(self.master, width=500, height=500)

        self.w.pack()
        self.master.update()

        # Draw a backing and lines
        x1, y1 = self._map_coords(0, 0)
        x2, y2 = self._map_coords(width, height)
        self.w.create_rectangle(x1, y1, x2, y2, fill = "white")

        # Draw tiles where car is
        self.tiles = {}
        # x1, y1 = self._map_coords(0, 0)
        # x2, y2 = self._map_coords(1, 1)
        self.tiles[()] = self.w.create_rectangle(self._map_coords(0, 3), self._map_coords(2, 4),
                                                             fill = "red")
        self.tiles[()] = self.w.create_rectangle(self._map_coords(1, 5), self._map_coords(3, 6),
                                                             fill = "blue")
        self.tiles[()] = self.w.create_rectangle(self._map_coords(2, 3), self._map_coords(3, 5),
                                                             fill = "yellow")
        self.tiles[()] = self.w.create_rectangle(self._map_coords(2, 2), self._map_coords(4, 3),
                                                            fill = "green")

        # Draw gridlines
        for i in range(width + 1):
            x1, y1 = self._map_coords(i, 0)
            x2, y2 = self._map_coords(i, height)
            self.w.create_line(x1, y1, x2, y2)
        for i in range(height + 1):
            x1, y1 = self._map_coords(0, i)
            x2, y2 = self._map_coords(width, i)
            self.w.create_line(x1, y1, x2, y2)

    def _map_coords(self, x, y):
        "Maps grid positions to window positions (in pixels)."
        return (250 + 450 * ((x - self.width / 2.0) / self.max_dim),
                250 + 450 * ((self.height / 2.0 - y) / self.max_dim))

    # root = Tk()
    #
    # def key(event):
    #     print "pressed", repr(event.char)
    #
    # def callback(event):
    #     frame.focus_set()
    #     print "clicked at", event.x, event.y
    #
    #     frame = Frame(root, width=100, height=100)
    #     frame.bind("<Key>", key)
    #     frame.bind("<Button-1>", callback)
    #     frame.pack()
    #
    #     root.mainloop()
    # if __name__ == "__main__":
    #     app = ExampleApp(board)
    #     app.mainloop()

    def done(self):
        "Indicate that the animation is done so that we allow the user to close the window."
        mainloop()
