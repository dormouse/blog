#!/usr/bin/python
# -*- coding: utf8 -*-

from gi.repository import Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        # 间隔为6
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        # 从左向右排
        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)
        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

        # 从右向左排
        self.button3 = Gtk.Button(label="I am 3")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.pack_end(self.button3, True, True, 0)
        self.button4 = Gtk.Button(label="I am 4")
        self.button4.connect("clicked", self.on_button4_clicked)
        self.box.pack_end(self.button4, True, True, 0)

    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Goodbye")

    def on_button3_clicked(self, widget):
        print("I am 3")

    def on_button4_clicked(self, widget):
        print("I am 4")

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
