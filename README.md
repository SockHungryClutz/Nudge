# Nudge Extension - Krita 4

Extension that allows you to nudge layers or selection areas around by 1 pixel at a time


## How to Install

 1. Open Krita, go to Settings->Manage Resources...->Open Resource Folder
 2. Open the pykrita folder inside the folder that pops up
 3. Download this repository and save the files and folders exactly as they are to the pykrita folder
 4. Copy the contents of the 'actions' directory into the actions folder that's next to the pykrita folder
 5. Close and reopen Krita
 6. Go to Settings->Configure Krita->Python Plugin Manager
 7. Scroll down and enable Nudge, click OK to save
 8. Close and reopen Krita again

You may need to reconfigure your keyboard shortcuts since up/down/left/right are bound by default to moving the path tool

## How to Use

Use the arrow keys to nudge the current layer around 1 pixel at a time.

###Other Notes

I originally wanted this plugin to nudge selection areas/selected content around too, but either the documentation for selections is wrong in many places, or there are many bugs/unintended behaviors with scripting selection.
