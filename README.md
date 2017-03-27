COMP-3000 Project: Nautilus Mass File Renamer
Authors:
- Matthew Walker 100980836
- Devon Witol 100??????

How to install:
- Copy 'Nautilus_mass_file_renamer.py' to ~/.local/share/nautilus/scripts 
  and give permission to execute file as a program

How to use:
- Select all the files that you want to rename
- Right click and under the Scripts tab, select 'Nautilus_mass_file_renamer.py'
- Input text that each file will have in their names
- Currently each file will be named with the users input, plus a unique number

Current functionality:
- Can rename multiple files simultaneously
- Checks for filename extensions
- Appends a unique number at the end of each file after an underscore
- Checks for blank input
- Checks for invalid characters

TO-DO:
- Improve window to include more options such as:
	- choice on what unique characters are added
	- choice on what goes between prefix and unique characters
	- choice on what parts of original filename are overwritten