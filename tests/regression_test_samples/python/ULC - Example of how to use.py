import wx
import wx.lib.agw.ultimatelistctrl as ULC

print wx.version()


class Frame(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)

        self.list = ULC.UltimateListCtrl(self, 
                                         agwStyle=ULC.ULC_REPORT
                                                 |ULC.ULC_HAS_VARIABLE_ROW_HEIGHT
                                                 |ULC.ULC_VRULES
                                                 |ULC.ULC_HRULES)

        # Define the columns
        self.list.InsertColumn(0, "AA")
        self.list.InsertColumn(1, "BB")
        self.list.InsertColumn(2, "CC")
        self.list.InsertColumn(3, "DD", width=124)

        # add some rows
        self.addRow(["one", "two", "three", "four"])
        self.addRow(["five", "six", "seven", "eight"])
        
                
    def addRow(self, values):
        row = self.list.GetItemCount()
        
        # First we create the new row/item (setting the value for the first column
        # at the same time)
        self.list.InsertStringItem(row, values[0])
        
        # Then we can set the values for the other columns of the same item.
        #    some normal string columns
        self.list.SetStringItem(row, 1, values[1])
        self.list.SetStringItem(row, 2, values[2])
        
        #    and a widget in this column
        tc = wx.TextCtrl(self.list, value=values[3], size=(120,-1))
        self.list.SetItemWindow(row, 3, tc)
        
        

app = wx.App(False)
frm = Frame(None, title="ULC Test")
frm.Show()
app.MainLoop()

    
