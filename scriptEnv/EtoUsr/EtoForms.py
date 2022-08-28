import clr
clr.AddReferenceByName("Eto")
clr.AddReferenceByName("Rhino.UI")

import Rhino
import scriptcontext
import System
import Rhino.UI
import Eto.Drawing as drawing
import Eto.Forms as forms

 
class EtoDialog(forms.Dialog[bool]):
 
    # Dialog box Class initializer
    def __init__(self):
        # Initialize dialog box
        self.Title = 'Glare Furniture: Number of Occupants'
        self.Padding = drawing.Padding(10)
        self.Resizable = False
 
        # Create controls for the dialog
        self.m_label = forms.Label(Text = 'Enter the Number of Occupants:')
        self.m_textbox = forms.TextBox(Text = None)
 
        # Create the default button
        self.DefaultButton = forms.Button(Text = 'OK')
        self.DefaultButton.Click += self.OnOKButtonClick
 
        # Create the abort button
        self.AbortButton = forms.Button(Text = 'Cancel')
        self.AbortButton.Click += self.OnCloseButtonClick
 
        # Create a table layout and add all the controls
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(5, 5)
        layout.AddRow(self.m_label, self.m_textbox)
        layout.AddRow(None) # spacer
        layout.AddRow(self.DefaultButton, self.AbortButton)
 
        # Set the dialog content
        self.Content = layout
 
    # Start of the class functions
 
    # Get the value of the textbox
    def GetText(self):
        return self.m_textbox.Text
 
    # Close button click handler
    def OnCloseButtonClick(self, sender, e):
        self.m_textbox.Text = ""
        self.Close(False)
 
    # OK button click handler
    def OnOKButtonClick(self, sender, e):
        if self.m_textbox.Text == "":
            self.Close(False)
        else:
            self.Close(True)
 
    ## End of Dialog Class ##


################################################################################
# The script that will be using the dialog.
def requestOccupantNumber():
    dialog = EtoDialog()
    rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)
    if (rc):
        return dialog.GetText() #Print the Number from the dialog control
 
