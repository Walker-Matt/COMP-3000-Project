#!/usr/bin/python
import os
import sys
from Tkinter import *

INVALID_NAME_CHARS = ('<', '>', ':', '"', '/', '\\', '|', '?', '*', '%', '+')

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
    splitList = original.split('.')
    fileType = splitList[len(splitList)-1]
    name = "%s.%s" % (name, fileType)

  return name

def getName():
  root = Tk()
  window = Window(root)
  root.mainloop()
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

    #Label for above input box
    self.entryLabel = Label(view, text="Please enter a prefix")

    #Input box for filename prefix
    self.entry = StringVar()
    vcmd = view.register(self.validate)
    self.entry = Entry(view, validate="key", validatecommand=(vcmd, '%P'))

    #Enter button to finish
    self.enterButton = Button(view, text="Enter", state='disabled', command=view.quit)

    #Grid layout for the window
    self.entryLabel.grid(row=0, column=0, columnspan=3, sticky=N)
    self.entry.grid(row=1, column=0, columnspan=2, sticky=W)
    self.enterButton.grid(row=1, column=1, sticky=E)

  def exited(self):
    self.exited = True
    self.view.quit()

  def validate(self, text):
    #Check fpr blank entry
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

  def getEntry(self):
    return self.entry

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))