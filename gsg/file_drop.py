#!/usr/bin/env python
"""

Getter Setter Generator

Sam Zielke-Ryner (samzielkeryner@gmail.com)

"""


import wx


class FileDrop( wx.FileDropTarget ):

    ## Class Functions: ##

    def __init__( self, _window, _parent_frame ):
        """ Constructor:  """

        wx.FileDropTarget.__init__( self )

        self.window       = _window
        self.parent_frame = _parent_frame


    def OnDropFiles( self, x, y, fileNames ):
        """ Post: This function is called when a file is dragged & dropped
                  onto the input TextCtrl widget. This function informs
                  the View component that the source code has been changed
                  (if it is valid). """

        # if a folder/directory has not been dropped onto the window/TextCtrl
        if len( fileNames ) == 1:

            # event = wx.DropFilesEvent( id=wx.wxEVT_DROP_FILES, noFiles=len(fileNames), file=fileNames[0] )
            self.parent_frame.notify_file_drop( fileNames[0] )

        else:

            self.parent_frame.show_error_dialog( "Input must be a single file & not a directory. \nPlease try again" )






