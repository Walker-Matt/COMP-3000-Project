#!/usr/bin/python
import os
import sys
from Tkinter import *

INVALID_NAME_CHARS = ('<', '>', ':', '"', '/', '\\', '|', '?', '*', '%', '+')

def main(files):
  if not files:
      return

  #Create the window
  root = Tk()
  window = Window(root, files)
  root.mainloop()

  entry = getName(window)
  isNumeric = window.numeric.get()
  isAlpha = window.alpha.get()
  
  unique = getUnique(0, isNumeric, isAlpha)

  for file in files:
    oldName = os.path.split(file)
    newName = None

    while not newName or (os.path.isfile(newName) and file != newName):
      name = setName(oldName[1], entry, str(unique))
      newName = os.path.join(oldName[0], name)
      unique = getUnique(unique, isNumeric, isAlpha)

    os.rename(file, newName)

def setName(original, entry, unique):
  name = "%s_%s" % (entry, unique)

  #check for file type extension
  fileType = getType(original)
  if fileType:
    name = "%s%s" % (name, fileType)

  return name

def getType(filename):
  if '.' in filename:
    splitName = filename.split('.')
    fileType = '.' + splitName[len(splitName)-1]
    return fileType
  else:
    return None

def getUnique(old, isNumeric, isAlpha):
  #Alphabetical
  if(isAlpha and not isNumeric):
    if(old == 0):
      new = 'A'
      return new

    charList = list(old)
    length = len(charList)

    #Handle all 'Z' cases
    if('Z' in charList):
      index = length - 1
      while(index != -1):
        if(charList[index] == 'Z'):
          charList[index] = 'A'
          if((index != 0) & (charList[index-1] != 'Z')):
            charList[index-1] = chr(ord(charList[index-1]) + 1)
            break
          if(index == 0):
            charList += 'A'
        elif(charList[index] != 'Z'):
          charList[index] = chr(ord(charList[index]) + 1)
          break
        index -= 1
      return "".join(charList)

    else:
      charList[length-1] = chr(ord(charList[length-1]) + 1)
      return "".join(charList)

  #Numerical
  else:
    new = old + 1
    return new

def getName(window):
  if window.exited:
    sys.exit()
  else:
    return window.entry

class Window():
  def __init__(self, view, files):
    self.view = view
    self.files = files
    view.protocol('WM_DELETE_WINDOW', self.exited)
    view.resizable(width=False, height=False)
    self.exited = False
    colour = "tomato"

    #Window parameters
    view.title("Nautilus Mass File Renamer")
    windowX = 300 #Width
    windowY = 275 #Height
    screenX = view.winfo_screenwidth()
    screenY = view.winfo_screenheight()
    WSX = (screenX/2) - (windowX/2)
    WSY = (screenY/2) - (windowY/2)
    view.geometry("%dx%d+%d+%d" % (windowX, windowY, WSX, WSY))

    #Label for above input box
    self.entryLabel = Label(view, text="Please enter a prefix")
    self.entryLabel.pack()
    self.entryLabel.place(anchor=N, x=150, y=5)

    #Input box for filename prefix
    self.entry = StringVar()
    vcmd = view.register(self.validate)
    self.entry = Entry(view, validate="key", validatecommand=(vcmd, '%P'))
    self.entry.pack()
    self.entry.place(anchor=W, x=45, y=40)

    #Label for checkboxes
    self.checkboxLabel = Label(view, text="Ordering\nstyle:")
    self.checkboxLabel.pack()
    self.checkboxLabel.place(anchor=W, x=35, y=70)

    #Checkbox for numeric ordering
    self.numeric = IntVar()
    self.numericCheckbox = Checkbutton(view, variable=self.numeric, 
                                      text="Numeric", onvalue=1, offvalue=0,
                                      command=self.toggleNumeric)
    self.numericCheckbox.pack()
    self.numericCheckbox.place(anchor=W, x=90, y=70)
    self.numericCheckbox.select()
    self.numericCheckbox.config(state="disabled")

    #Checkbox for alphabetical ordering
    self.alpha = IntVar()
    self.alphaCheckbox = Checkbutton(view, variable=self.alpha, 
                                    text="Alphabetical", onvalue=1, offvalue=0,
                                    command=self.toggleAlpha)
    self.alphaCheckbox.pack()
    self.alphaCheckbox.place(anchor=W, x=165, y=70)

    #Enter button to finish
    self.enterButton = Button(view, text="Enter", state='disabled', command=view.quit,
                              activebackground=colour)
    self.enterButton.pack()
    self.enterButton.place(anchor=E, x=255, y=40)

    #Scrollbar for both lists
    self.listScrollBar = Scrollbar(view, command=self.scrollLists)
    self.listScrollBar.pack(side="right", fill="y")

    #Label for selected files list
    self.oldLabel = Label(view, text="Old Name", relief=RIDGE, width=16, bg=colour)
    self.oldLabel.pack()
    self.oldLabel.place(anchor=W, x=10, y=100)

    #list of all selected files
    self.oldNameList = Listbox(view, width=16, yscrollcommand=self.scroll)
    self.oldNameList.bind("<MouseWheel>", self.mouseWheel)
    self.oldNameList.pack()
    self.oldNameList.place(anchor=W, x=10, y=185)
    index = 1
    for file in self.files:
      self.oldNameList.insert(index, file)
      index += 1

    #Arrows to show relation between lists
    self.arrow = Listbox(view, width=1, relief=FLAT, bg="light grey")
    self.arrow.pack()
    self.arrow.place(anchor=W, x=141, y=185)
    num = 10
    while(num != 0):
      self.arrow.insert(11-num, ">")
      num -= 1

    #Label for selected files list
    self.newLabel = Label(view, text="New Name", relief=RIDGE, width=16, bg=colour)
    self.newLabel.pack()
    self.newLabel.place(anchor=E, x=284, y=100)

    #List of all renamed files
    self.newNameList = Listbox(view, width=16, yscrollcommand=self.scroll)
    self.newNameList.bind("<MouseWheel>", self.mouseWheel)
    self.newNameList.pack()
    self.newNameList.place(anchor=E, x=284, y=185)

  def exited(self):
    self.exited = True
    self.view.quit()  

  def validate(self, text):
    #Check for blank entry
    if not text:
      self.entry = text
      self.updateList(text)
      self.enterButton.config(state="disabled")
      return True
    #Check for name starting with a '.' (hidden file)
    textChars = text.split()
    if textChars[0] == '.':
      return False
    #Check for invalid filename characters
    for char in INVALID_NAME_CHARS:
      if char in text:  
        return False

    self.entry = text
    self.updateList(text)
    self.enterButton.config(state="normal")
    return True

  def toggleNumeric(self):
    self.alphaCheckbox.config(state="normal")
    self.alphaCheckbox.deselect()
    self.numericCheckbox.config(state="disabled")
    self.updateList(self.entry)

  def toggleAlpha(self):
    self.numericCheckbox.config(state="normal")
    self.numericCheckbox.deselect()
    self.alphaCheckbox.config(state="disabled")
    self.updateList(self.entry)

  def updateList(self, text):
    if(text):
      index = 1
      size = len(self.files)
      self.newNameList.delete(0, size)
      unique = getUnique(0, self.numeric.get(), self.alpha.get())
      for file in self.files:
        fileType = getType(file)
        if not fileType:
          fileType = ""
        newName = self.entry + "_" + str(unique) + fileType
        unique = getUnique(unique, self.numeric.get(), self.alpha.get())
        self.newNameList.insert(index, newName)
        index += 1
    else:
      size = len(self.files)
      self.newNameList.delete(0, size)

  def scrollLists(self, *args):
    self.oldNameList.yview(*args)
    self.newNameList.yview(*args)

  def mouseWheel(self, event):
    if(event == "<MouseWheel>"):
      self.scrollLists("scroll", event.delta,"units")
      return "break"

  def scroll(self, *args):
    self.listScrollBar.set(*args)
    units = str(float(args[0]))
    self.newNameList.yview_moveto(units)
    self.oldNameList.yview_moveto(units)

  def getEntry(self):
    return self.entry

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))