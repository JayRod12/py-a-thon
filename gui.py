from tkinter import Tk, BOTH, Menu, Toplevel
from tkinter.ttk import Frame, Button, Style

def donothing(parent):
  filewin = Toplevel(parent)
  button = Button(filewin, text="Do nothing button")
  button.pack()

class MainScreen(Frame):

  def __init__(self, parent):
    Frame.__init__(self, parent)
    self.parent = parent
    self.initUI()
  def initUI(self):
    self.parent.title("Agilent 8642 A")
    self.pack(fill=BOTH, expand=1)
    self.setupWindow(self.parent)
    self.setupMenubar(self.parent)

  def setupMenubar(self, root):
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing(root))
    filemenu.add_command(label="Open", command=donothing(root))
    filemenu.add_command(label="Save", command=donothing(root))
    filemenu.add_command(label="Save as...", command=donothing(root))
    filemenu.add_command(label="Close", command=donothing(root))
    
    filemenu.add_separator()
    
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing(root))
    
    editmenu.add_separator()
    
    editmenu.add_command(label="Cut", command=donothing(root))
    editmenu.add_command(label="Copy", command=donothing(root))
    editmenu.add_command(label="Paste", command=donothing(root))
    editmenu.add_command(label="Delete", command=donothing(root))
    editmenu.add_command(label="Select All", command=donothing(root))
    
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing(root))
    helpmenu.add_command(label="About...", command=donothing(root))
    menubar.add_cascade(label="Help", menu=helpmenu)
    
    root.config(menu=menubar)
    root.mainloop() 

  def toggle_geom(self,event):
    # Set up full screen frame
     geom=self.parent.winfo_geometry()
     #print(geom,self._geom)
     self.parent.geometry(self._geom)
     self._geom=geom
  def setupWindow(self, parent):
    pad=3
    self._geom='500x500+0+0'
    parent.geometry("{0}x{1}+0+0".format(
        parent.winfo_screenwidth()-pad, parent.winfo_screenheight()-pad))
    parent.bind('<Escape>',self.toggle_geom)            

def main():
  root = Tk()
  mainScreen = MainScreen(root)
  root.mainloop()

if __name__ == '__main__':
  main()

