#!/usr/bin/python3
# -*- coding:utf-8 -*-
#
# Copyright © 2020, 2021 cGIfl300
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
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


from datetime import datetime, timedelta
from tkinter import Tk, Label, Button, PhotoImage

import pygame


class Alarm(Tk):
    # Graphic interface ...
    def __init__(self):
        Tk.__init__(self)
        self.pomodoro = 20  # How many minutes for a pomodoro
        self.long_break = 15  # How many minutes for a pomodoro
        self.short_break = 5  # How many minutes for a long break
        self.tick_timeout = 500  # Tick minimum timeout in ms
        self.timer_counter = 0  # Timer counter
        self.repeat_bell = 0  # Number of recall of the ring
        self.next_timeout = datetime.now()
        self.working_color = "green"
        self.break_color = "blue"
        self.working = True

        # Some about multimedia
        pygame.mixer.init()
        self.enjoy_the_sound = pygame.mixer.Sound("data/church_bell.ogg")

        # Components placing
        self.lbl = Label(text="Here I am.")
        self.lbl.pack(fill="x")
        self.lbl_info = Label(text="00:00")
        self.lbl_info.pack(fill="x")

        self.btn_sound = Button(
            command=self.enjoy_the_sound.stop,
            text="Stop the noise",
            relief="flat",
            bd=1,
        )
        self.btn_sound.pack(fill="both")
        self.btn = Button(
            command=self.destroy,
            text="May I, please,\n" "leave this\n" "marvelous software",
            relief="flat",
            bd=1,
        )
        self.btn.pack(fill="both")

    def interface(self):
        # Window interface

        self.title("alarm")
        self.iconphoto(False, PhotoImage(file="images/icon.png"))
        self.__apply_colors()
        self.after(self.tick_timeout, self.__tick())

    def __apply_colors(self):
        if self.working:
            self.lbl.config(bg=self.working_color)
            self.lbl_info.config(bg=self.working_color)

            self.btn.config(background=self.working_color)
            self.btn.config(activebackground=self.break_color,
                            highlightbackground=self.working_color)

            self.btn_sound.config(background=self.working_color)
            self.btn_sound.config(activebackground=self.break_color,
                                  highlightbackground=self.working_color)
        else:
            self.lbl.config(bg=self.break_color)
            self.lbl_info.config(bg=self.break_color)

            self.btn.config(background=self.break_color)
            self.btn.config(activebackground=self.working_color)

            self.btn_sound.config(background=self.break_color,
                                  highlightbackground=self.break_color)
            self.btn_sound.config(activebackground=self.working_color,
                                  highlightbackground=self.break_color)

    def __print_timeout(self, message):
        self.__apply_colors()
        self.lbl_info.config(
            text=(str((self.next_timeout - datetime.now()))[2:-7]))
        self.lbl.config(text=message)

    def __tick(self):
        if datetime.now() > self.next_timeout:
            self.__timeout()
        self.lbl_info.config(
            text=str((self.next_timeout - datetime.now()))[2:-7])
        self.after(self.tick_timeout, self.__tick)

    def __play_sound(self):
        self.enjoy_the_sound.play(loops=self.repeat_bell)

    def __timeout(self):
        # Timeout
        self.timer_counter += 1
        self.__play_sound()
        if self.timer_counter == 1:
            self.working = True
            self.repeat_bell = self.pomodoro - 1
            self.__print_timeout(f"Let's work for {self.pomodoro} minutes.")
            self.next_timeout = datetime.now() + timedelta(
                minutes=self.pomodoro)
        elif self.timer_counter == 2:
            self.working = False
            self.repeat_bell = self.short_break - 1
            self.__print_timeout(
                f"Let's work for {self.short_break} minutes.")
            self.next_timeout = datetime.now() + timedelta(
                minutes=self.short_break)
        elif self.timer_counter == 3:
            self.working = True
            self.repeat_bell = self.pomodoro - 1
            self.__print_timeout(f"Let's work for {self.pomodoro} minutes.")
            self.next_timeout = datetime.now() + timedelta(
                minutes=self.pomodoro)
        elif self.timer_counter == 4:
            self.working = False
            self.repeat_bell = self.short_break - 1
            self.__print_timeout(
                f"Let's work for {self.short_break} minutes.")
            self.next_timeout = datetime.now() + timedelta(
                minutes=self.short_break)
        elif self.timer_counter == 5:
            self.working = True
            self.repeat_bell = self.pomodoro - 1
            self.__print_timeout(f"Let's work for {self.pomodoro} minutes.")
            self.next_timeout = datetime.now() + timedelta(
                minutes=self.pomodoro)
        elif self.timer_counter == 6:
            self.working = False
            # This is the last one, one ring will be
            self.repeat_bell = self.long_break - 2
            # auto added
            self.__print_timeout(
                f"Let's work for {self.long_break} minutes.")
            self.next_timeout = datetime.now() + timedelta(
                minutes=self.long_break)
        elif self.timer_counter == 7:
            self.timer_counter = 0
            self.repeat_bell = 0
            self.next_timeout = datetime.now()
        pass

    def run(self):
        self.interface()
        self.mainloop()


if __name__ == "__main__":
    app = Alarm()
    app.run()
