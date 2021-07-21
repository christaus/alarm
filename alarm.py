# -*- coding:utf-8 -*-
#
# Copyright © 2020 cGIfl300
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the “Software”),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from datetime import datetime, timedelta
from time import sleep
from tkinter import *


class Alarm(Tk):
    # Graphic interface ...

    def __init__(self):
        Tk.__init__(self)
        self.pomodoro = 20  # How many minutes for a pomodoro
        self.long_break = 15  # How many minutes for a pomodoro
        self.short_break = 5  # How many minutes for a long break
        self.tick_timeout = 500  # Tick minimum timeout in ms
        self.timer_counter = 0  # Timer counter
        self.next_timeout = datetime.now()

        # Components placing
        self.lbl = Label(text="Here I am.")
        self.lbl.pack()
        self.lbl_info = Label(text="00:00")
        self.lbl_info.pack()
        self.btn = Button(command=self.destroy, text="Fin du monde.")
        self.btn.pack()

    def interface(self):
        # Window interface

        self.title('alarm')
        self.iconphoto(False, PhotoImage(file="images/icon.png"))
        self.after(self.tick_timeout, self.__tick())

    def __print_timeout(self, message):
        self.lbl_info.config(
            text=(str((self.next_timeout - datetime.now()))[2:-7]))
        self.lbl.config(text=message)

    def __tick(self):
        if datetime.now() > self.next_timeout:
            self.__timeout()
        self.lbl_info.config(
            text=str((self.next_timeout - datetime.now()))[2:-7])
        self.after(self.tick_timeout, self.__tick)

    def __timeout(self):
        # Timeout
        self.timer_counter += 1
        if self.timer_counter == 1:
            self.__print_timeout("Let's work for 20 minutes.")
            self.next_timeout = datetime.now() + timedelta(minutes=20)
        elif self.timer_counter == 2:
            self.__print_timeout("Have your second 5 minutes break.")
            self.next_timeout = datetime.now() + timedelta(minutes=5)
        elif self.timer_counter == 3:
            self.__print_timeout("Let's work for 20 minutes.")
            self.next_timeout = datetime.now() + timedelta(minutes=20)
        elif self.timer_counter == 4:
            self.__print_timeout("Have your second 5 minutes break.")
            self.next_timeout = datetime.now() + timedelta(minutes=5)
        elif self.timer_counter == 5:
            self.__print_timeout("Let's work for 20 minutes.")
            self.next_timeout = datetime.now() + timedelta(minutes=20)
        elif self.timer_counter == 6:
            self.__print_timeout("Have a long 15 minutes break now.")
            self.next_timeout = datetime.now() + timedelta(minutes=15)
        elif self.timer_counter == 7:
            self.timer_counter = 0
            self.next_timeout = datetime.now()
        pass

    def run(self):
        self.interface()
        self.mainloop()


if __name__ == '__main__':
    app = Alarm()
    app.run()
