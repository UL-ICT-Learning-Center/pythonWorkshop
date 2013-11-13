#!/usr/bin/python2

import gtk

def printHello(buttonInstance):
  print('Button says hi')

win = gtk.Window()
win.connect("delete-event", gtk.main_quit)

# add a button to the UI
button = gtk.Button("Hello World")
button.connect( "clicked", printHello )

win.add( button )

win.set_default_size( 400, 250 )
win.show_all()

gtk.main()
