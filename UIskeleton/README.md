# Presentation Layer & View Layer
**OVERVIEW:**

The UIskeleton File is the presentation/view layer of this software project.
Every thing included in this file deals with the actual GUI ie. buttons on the 
screen or other widgets. A separate layer encapsulated in another file deals with
the control of the modules in this file. 

**CONVENTIONS:**

Some of the windows in this file are "simple windows" that that publicly inherit 
from QtWidget and do not need any other implementation steps to integrate into the 
project. The "simple windows" are welcomeUI.py and loadingUI.py. 

The remaining windows are more complex because they were designed using QtDesigner.
The Designer creates a GUI implementation that's a standalone representation of what 
came out of the Designer software. To add additional functionality or include into a 
bigger project the UI files need to use multiple inheritance in order to be included.

Files ending with UI are base classes. Files ending with APP are the multiple inheritance 
classes. The UI files are the base implementation and the APP files makes the additional 
signal connections are implemented in the files with APP suffix.      