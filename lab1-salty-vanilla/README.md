# Lab 1 : Passive Network Measurement
  
For this lab, you may work solo or with one other partner of your choice.
You are not allowed to copy or look at code from other teams. However,
you are welcome to discuss the assignments with any students without sharing code.

## Team Info

Partner A: Name (UTEID)

Partner B: Name (UTEID)

(Note once the team is formed, you may not leave the team as code base is very small.)

### Check Course Calendar/Canvas for Due Dates
By **checkpoint** deadline
* Fill out the team info above and push this updated README to your team repository.
* Also make sure to submit the URL of your team repository.
* Complete `TODO 1` through `TODO 6` in `Lab1_Notebook.ipynb` and push the updated notebook (and other updated files) to your team repository.

By **final** deadline
* Complete the rest of the `TODOs` in `Lab1_Notebook.ipynb`.
* Push the updated notebook (and other updated fileds) to your team repository.

## Getting Started

#### Step 1.
ssh into a CS machine and run the following command.
```
cshost$ cd {YourFolderName}
cshost$ git clone https://github.com/cs356-sp22/lab1-{YourTeamName}
cshost$ jupyter-notebook --no-browser
```
With the command above you should see jupter notebook running on the CS machine and it will output a URL that looks like below.
```
http://localhost:8888/?token={SomeLongString}
```
Copy this URL to a clipboard. 

#### Step 2.
On your off campus local machine run the following command in the terminal.
```
local$ ssh -L 8888:localhost:8888 {YourCSUserName}@{cshost}.cs.utexas.edu
```
You need to replace {YourCSUserName} and {cshost} accordingly, where {cshost} is the machine that you used in Step 1. 

#### Step 3.
On your local machine, open up a browser and type the URL that you obtained in Step 1 after running jupyter-notebook command including the token string.

This should open to the Jupyter notebook file selection window.  Juypter notebook is actually running on port
8888 on the cs machine but you can access it through your local machine browser.

In the file selection window, enter the `lab1-{YourTeamName}` directory and 
navtigate to `Lab1_Notebook.ipynb` and open the notebook. 

You will see the instructions for the rest of the assignment.  Work through this notebook from top to bottom and complete the sections marked "TODO."

**Remember to "Save and Checkpoint" (from the "File" menu) before you leave the
notebook or close your tab.**  

## Jupyter Notebook

Jupyter Notebook (formerly called iPython Notebook) is a browser-based IDE with
a cell-based editor.

Every cell in a notebook can contain either code or text ("Markdown"). Begin
editing a cell by double-clicking it. You can execute the code in a cell (or
typeset the text) by pressing `shift-enter` with the cell selected.  Global
variables and functions are retained across cells. Save your work with the
"Save and Checkpoint" option in the "File" menu. If your code hangs, you can
interrupt it with the "Interrupt" option in the "Kernel" menu.  You can also
clear all variables and reset the environment with the "Restart" option in the
"Kernel" menu.

The "Help" menu contains many additional resources about Jupyter notebooks
(including a user interface tour, useful keyboard shortcuts, and links to
tutorials).

## Submission

TODO: Remember to put your names and eids in the marked location at the top of the
file. Push the updated files to the team repository.

#### Acknowledgement
This assignment is adopted from [Nick Feamster](https://computernetworksbook.com/resources.html).


