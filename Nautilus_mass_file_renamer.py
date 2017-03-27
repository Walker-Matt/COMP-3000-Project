#!/usr/bin/python
import os
import sys

TITLE = 'Nautilus_Mass_File_Renamer'
ZENITY = "zenity --entry '' --title " + TITLE
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

def getName():
  default = ZENITY + " --text 'Enter a prefix' --width 300"
  window = os.popen(default)
  entry = window.read()
  entry = entry.split('\n')[0]
  window.close()

  invalid = True
  while invalid or (not entry):
    #Check for blank input
    if not entry:
      blank = ZENITY + " --text 'No prefix entered' --width 300"
      window = os.popen(blank)
      entry = window.read()
      entry = entry.split('\n')[0]
      window.close()

    #Check for invalid chars
    for char in INVALID_NAME_CHARS:
      if char in entry:
        #Backslashes are special...
        if char == '\\':
          invalid = ZENITY + (" --text 'Cannot contain a backslash' --width 300")
        else:
          invalid = ZENITY + (" --text 'Cannot contain: %s' --width 300" % char)
        window = os.popen(invalid)
        entry = window.read()
        entry = entry.split('\n')[0]
        window.close()
        invalid = True
        break
      else:
        invalid = False

  return entry

def setName(original, entry, unique):
  name = "%s_%s" % (entry, unique)

  #check for file type extension
  if '.' in original:
    fileType = original.split('.')[-1]
    name = "%s.%s" % (name, fileType)

  return name

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))