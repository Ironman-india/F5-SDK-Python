# !/usr/bin/python3
from tkinter import *

root=Tk()
root.title("Automated Configuration Manager")
#txt = Text(root)
#txt.insert(INSERT,"Automated Configuration Manager")
#txt.pack()
menubar = Menu(root)
devicemenu = Menu(menubar, tearoff = 0)
terminalmenu = Menu(menubar, tearoff = 0)
helpmenu = Menu(menubar, tearoff = 0)
f5menu = Menu(devicemenu, tearoff = 0)
netsealermenu = Menu(devicemenu, tearoff = 0)
createmenu = Menu(f5menu, tearoff = 0)
menubar.add_cascade(label = "Devices", menu = devicemenu)
menubar.add_cascade(label = "Terminal", menu = terminalmenu)
menubar.add_cascade(label = "Help", menu = helpmenu)
devicemenu.add_cascade(label = "F5", menu = f5menu)
devicemenu.add_cascade(label = "Net Scalar", menu = netsealermenu)
f5menu.add_cascade(label = "Create", menu = createmenu)
createmenu.add_command(label = "VIP")
createmenu.add_command(label = "Pool")
createmenu.add_command(label = "Node")
netsealermenu.add_command(label = "Crease")
root.config(menu = menubar)
root.mainloop()

