# Binding Events
'''
Most of this file consists of callback handler functions triggered when bound events
occur. 

this type of callback receives an event object argument that gives details about the event that fired. 

Technically, this argument is an instance of the tkinter Event class, and its details are attributes; 
most of the callbacks simply trace events by displaying relevant event attributes.
'''

'''
First, some definitions: tkinter.pdf
• An event is some occurrence that your application needs to know about.
• An event handler is a function in your application that gets called when an event occurs.
• We call it binding when your application sets up an event handler that gets called when an event
happens to a widget.
'''

from tkinter import *

def showPosEvent(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))

    # For mouse-related events, callbacks print the X and Y coordinates of the mouse pointer,
	# in the event object passed in.
	# Coordinates are usually measured in pixels from the
	# upper-left corner (0,0), but are relative to the widget being clicked.

def showAllEvent(event):
    print(event)
    for attr in dir(event):
        if not attr.startswith('__'): 
            print(attr, '=>', getattr(event, attr))

    # the middle-click callback dumps the entire argument—all of the Event object’s attributes 
    # (less internal names that begin with “__” which includes the __doc__ string, 
    # and default operator overloading methods inherited from the implied object superclass

def onKeyPress(event):
    print('Got key press:', event.char)

def onArrowKey(event):
    print('Got up arrow key press')

def onReturnKey(event):
    print('Got return key press')

def onLeftClick(event):
    print('Got left mouse button click:', end=' ')
    showPosEvent(event)

def onRightClick(event):
    print('Got right mouse button click:', end=' ')
    showPosEvent(event)

def onMiddleClick(event):
    print('Got middle mouse button click:', end=' ')
    showPosEvent(event)
    showAllEvent(event)

def onLeftDrag(event):
    print('Got left mouse button drag:', end=' ')
    showPosEvent(event)

def onDoubleLeftClick(event):
    print('Got double left mouse click', end=' ')
    showPosEvent(event)
    tkroot.quit()

tkroot = Tk()

labelfont = ('courier', 20, 'bold')                # family, size, style

widget = Label(tkroot, text='Hello bind world')

widget.config(bg='red', font=labelfont)            # red background, large font
widget.config(height=5, width=20)                  # initial size: lines,chars
widget.pack(expand=YES, fill=BOTH)

widget.bind('<Button-1>',  onLeftClick)            # mouse button clicks
widget.bind('<Button-3>',  onRightClick)
widget.bind('<Button-2>',  onMiddleClick)          # middle=both on some mice
widget.bind('<Double-1>',  onDoubleLeftClick)      # click left twice
widget.bind('<B1-Motion>', onLeftDrag)             # click left and move

widget.bind('<KeyPress>',  onKeyPress)             # all keyboard presses
widget.bind('<Up>',        onArrowKey)             # arrow button pressed
widget.bind('<Return>',    onReturnKey)            # return/enter key pressed

widget.focus()                                     # or bind keypress to tkroot

tkroot.title('Click Me')

tkroot.mainloop()

'''
Other bind Events
Besides those illustrated in this example, a tkinter script can register to catch additional
kinds of bindable events. For example:
• <ButtonRelease> fires when a button is released ( <ButtonPress> is run when the
button first goes down).
• <Motion> is triggered when a mouse pointer is moved.
• <Enter> and <Leave> handlers intercept mouse entry and exit in a window’s display
area (useful for automatically highlighting a widget).
• <Configure> is invoked when the window is resized, repositioned, and so on (e.g.,
the event object’s width and height give the new window size). We’ll make use of
this to resize the display on window resizes in the PyClock example of Chapter 11.
• <Destroy> is invoked when the window widget is destroyed (and differs from the
protocol mechanism for window manager close button presses). Since this inter-
acts with widget quit and destroy methods, I’ll say more about the event later in
this section.
• <FocusIn> and <FocusOut> are run as the widget gains and loses focus.
• <Map> and <Unmap> are run when a window is opened and iconified.
• <Escape> , <BackSpace> , and <Tab> catch other special key presses.
• <Down> , <Left> , and <Right> catch other arrow key presses.

This is not a complete list, and event names can be written with a somewhat sophisti-
cated syntax of their own. For instance:
• Modifiers can be added to event identifiers to make them even more specific; for
instance, <B1-Motion> means moving the mouse with the left button pressed, and
<KeyPress-a> refers to pressing the “a” key only.
• Synonyms can be used for some common event names; for instance, <Button
Press-1> , <Button-1> , and <1> mean a left mouse button press, and <KeyPress-a>
and <Key-a> mean the “a” key. All forms are case sensitive: use <Key-Escape> , not
<KEY-ESCAPE> .
• Virtual event identifiers can be defined within double bracket pairs (e.g., <<Paste
Text>> ) to refer to a selection of one or more event sequences.

'''