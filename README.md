COMP-3000 Project: Nautilus Mass File Renamer
Authors:
- Matthew Walker 100980836
- Devon Witol 100??????

How to install as a nautilus script:
- Copy 'Nautilus_mass_file_renamer.py' to ~/.local/share/nautilus/scripts 
  and give permission to execute file as a program

How to install as a new nautilus action:
- Install nautilus-actions with the command:
	- sudo apt-get install nautilus-actions
- Then open nautilus-actions from Dash and click 'define a new action'
- Title the action 'Mass rename' for example, in the context label box
- Under the 'Command' tab input the path of the script
	- Also include '%B' in the parameters box, to allow proper file input
- Then click 'Record all the modified actions'

How to use:
- Select all the files that you want to rename
- (As a script) Right click and under the Scripts tab, select 'Nautilus_mass_file_renamer.py'
- (As an action) Right click and select the 'Mass rename' action
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