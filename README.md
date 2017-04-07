COMP-3000 Project: Nautilus Mass File Renamer
Authors:
- Matthew Walker 100980836
- Devon Witol 100863082

Packages needed:
- latest version of python
- tkinter (python.tk)
- nautilus-actions
- RUN: sudo apt-get install python python-tk nautilus-actions

How to install as a nautilus script:
- Copy 'Nautilus_mass_file_renamer.py' to ~/.local/share/nautilus/scripts 
  and give permission to execute file as a program

How to install as a new nautilus action:
- Install nautilus-actions with the command:
	- sudo apt-get install nautilus-actions
- Then open nautilus-actions from Dash and click 'define a new action'
- Title the action 'Mass rename' for example, in the context label box
- Under the 'Command' tab, input the path of the script
	- Also include '%B' in the parameters box, to allow proper file input
- Then click 'Record all the modified actions'
- Restart nautilus to use the new action

How to use:
- Select all the files that you want to rename
- (As a script) Right click and under the Scripts tab, select 'Nautilus_mass_file_renamer.py'
- (As an action) Right click and select the 'Mass rename' action
- Input text that each file will have in their names
- Choose a file ordering style (default is numerical)

Current functionality:
- Can rename multiple files simultaneously
- Checks for filename extensions
- Appends a unique number at the end of each file after an underscore
- Checks for blank input
- Checks for invalid characters
- Choice on what unique characters are added (alphabetical or numerical)
- Lists filenames before and after renaming
- Choice on what goes between prefix and unique characters

TO-DO:
- Improve window to include more options such as:
	- choice on if the text is appended to the beginning or end
	- choice on what parts of original filename are overwritten