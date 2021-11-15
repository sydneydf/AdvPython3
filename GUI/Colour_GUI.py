import random
from tkinter import *
import colourise
import threading


class Colour_GUI:
    def __init__(self):
        # Our main Tkinter object
        self.main_window = Tk()

        # hoisting our variables with empties ready for later assignment
        self.colour_label = None
        self.inversed_label = None
        self.rgb_colours = []

        # Call our setup function
        self.init_main_window()

    def init_main_window(self):
        """
        @return: Initialize window components
        """

        # Fill rgb colours list up with random colours
        for i in range(11):
            self.rgb_colours.append([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

        # Set our labels up and pack them
        self.colour_label = Label(self.main_window, width=60, height=30)
        self.colour_label.pack()
        self.inversed_label = Label(self.main_window, width=60, height=30)
        self.inversed_label.pack()

        # Initiate change_colour thread
        self.change_colour()
        # activate the root element loop
        self.main_window.mainloop()

    def change_colour(self):
        """
        Setup a thread on this function name and start it
        assign random rgb from created list
        Get Hex value of the random colour
        Get Hex value of the inverse of the random colour
        open the selected label's config options and put the hex in
        @return:
        """

        threading.Timer(1.0, self.change_colour).start()
        rand_R, rand_G, rand_B = self.rgb_colours[random.randint(0, 9)]
        col_hex = self.RGB2Hex(rand_R, rand_G, rand_B)
        inverse_hex = self.Colour_Inverse(rand_R, rand_G, rand_B)
        self.colour_label.config(bg=col_hex, text=col_hex)
        self.inversed_label.config(bg=inverse_hex, text=inverse_hex)

    def RGB2Hex(self, _r: int, _g: int, _b: int) -> str:
        """
        @param _r: int
        @param _g: int
        @param _b: int
        @return: string representation of RGB code
        """
        return "#{:02x}{:02x}{:02x}".format(_r, _g, _b)

    def Colour_Inverse(self, _r: int, _g: int, _b: int) -> str:
        """
        @param _r: int
        @param _g: int
        @param _b: int
        @return: inverse rgb code using colourise.compliment_rgb function then passing rounded results to RGB2Hex
        """

        # IMPORTANT NOTE WITH .complement_rgb() returns decimal floats that without rounding will screw up alot of
        # functions that would take them with direct output

        inversed_R, inversed_G, inversed_B = colourise.complement_rgb(_r, _g, _b)
        return self.RGB2Hex(round(inversed_R), round(inversed_G), round(inversed_B))


GUI = Colour_GUI()
