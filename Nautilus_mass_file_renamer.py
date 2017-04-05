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
  window = Window(root)
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
  if '.' in original:
    splitList = original.split('.')
    fileType = splitList[len(splitList)-1]
    name = "%s.%s" % (name, fileType)

  return name

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
  def __init__(self, view):
    self.view = view
    view.protocol('WM_DELETE_WINDOW', self.exited)
    self.exited = False

    #Window parameters
    view.title("Nautilus Mass File Renamer")
    windowX = 300
    windowY = 100
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
    self.enterButton = Button(view, text="Enter", state='disabled', command=view.quit)
    self.enterButton.pack()
    self.enterButton.place(anchor=E, x=255, y=40)

  def exited(self):
    self.exited = True
    self.view.quit()  

  def validate(self, text):
    #Check for blank entry
    if not text:
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
    self.enterButton.config(state="normal")
    return True

  def toggleNumeric(self):
    self.alphaCheckbox.config(state="normal")
    self.alphaCheckbox.deselect()
    self.numericCheckbox.config(state="disabled")

  def toggleAlpha(self):
    self.numericCheckbox.config(state="normal")
    self.numericCheckbox.deselect()
    self.alphaCheckbox.config(state="disabled")

  def getEntry(self):
    return self.entry

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))