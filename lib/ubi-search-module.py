#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Edilson Alzemand

import gtk 
import webkit 
import sys

comand = sys.argv[1:]
s = ' '.join(comand)

s = s.replace(' ', '+')

view = webkit.WebView() 
win = gtk.Window(gtk.WINDOW_TOPLEVEL) 
win.set_title(' Ꙩ  ubi search')
win.set_size_request(1024,640)
win.set_resizable(True)
win.connect("destroy",gtk.main_quit)
win.add(view) 
win.show_all() 
win=gtk.Window()
view.open("https://www.google.com.br/?gws_rd=ssl#q=" + s) 
gtk.main()
