#!/usr/bin/python
import os
import sys
from Tkinter import *

INVALID_NAME_CHARS = ('<', '>', ':', '"', '/', '\\', '|', '?', '*', '&', '%')

def main(files):
  if not files:
      return

  #A unique number to append at the end of each filename
  uniqueNumber = 1
  entry = getName()

  for file in files:
    oldNames = os.path.split(file)
    newName = None

    while not newName or (os.path.isfile(newName) and file != newName):
      name = setName(oldNames[1], entry, str(uniqueNumber))
      newName = os.path.join(oldNames[0], name)
      uniqueNumber += 1

    os.rename(file, newName)

def setName(original, entry, unique):
  name = "%s_%s" % (entry, unique)

  #check for file type extension
  if '.' in original:
    fileType = original.split('.')[-1]
    name = "%s.%s" % (name, fileType)

  return name

def getName():
  root = Tk()
  window = Window(root)
  root.mainloop()
  return window.entry

class Window():
  def __init__(self, view):
    self.view = view

    #Window parameters
    view.title("Nautilus Mass File Renamer")
    #view.geometry("300x100")

    #Label for above input box
    self.entryLabel = Label(view, text="Please enter a prefix")
    self.entryLabel.pack()

    #Input box for filename prefix
    self.entry = StringVar()
    vcmd = view.register(self.validate)
    self.entry = Entry(view, validate="key", validatecommand=(vcmd, '%P'))
    self.entry.pack()

    #Enter button to finish
    self.enterButton = Button(view, text="Enter", command=view.quit)
    self.enterButton.pack()

  def validate(self, text):
    if not text:
      return False
    for char in INVALID_NAME_CHARS:
      if char in text:
        return False

    self.entry = text
    return True

  def getEntry(self):
    return self.entry

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))