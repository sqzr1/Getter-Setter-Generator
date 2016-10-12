#! /usr/bin/env python
from Tkinter import *
from RSSGenerator import *
import tkSimpleDialog
import tkMessageBox


class RSSSite:
    """An RSS Site"""
    def __init__(self, Name="", Url=""):
        self.Name = Name
        self.Url = Url

class RSSItemDialog(tkSimpleDialog.Dialog):

    def __init__(self, parent, title=None, RSSName="", RSSUrl=""):
        """Init, override default for default params"""
        self.RSSName = RSSName
        self.RSSUrl = RSSUrl
        self.Result = False #Default = Cancel
        tkSimpleDialog.Dialog.__init__(self, parent,title)
        
    def body(self, master):
        """This is where you create the Body of the dlg"""
 
        lbText = Label(master, text="Name")
        lbText.grid(row=0, padx=5, pady=10,sticky=W)
        lbText = Label(master, text="URL:")
        lbText.grid(row=1, padx=5,sticky=W)

        self.eRSSName = Entry(master)
        self.eRSSName.insert(0,self.RSSName)
        self.eRSSUrl = Entry(master)
        self.eRSSUrl.insert(0,self.RSSUrl)

        self.eRSSName.grid(row=0, column=1)
        self.eRSSUrl.grid(row=1, column=1)
        
        """Return the widget that will get focuds"""
        return self.eRSSName

    def apply(self):
        """They have selected OK"""
        self.Result = True
        self.RSSName = (self.eRSSName.get())
        self.RSSUrl = (self.eRSSUrl.get())
        
class GUIFramework(Frame):
    """This is the GUI"""
    
    def __init__(self,master=None):
        """Initialize yourself"""
        
        """Initialise the base class"""
        Frame.__init__(self,master)
        
        """Set the Window Title"""
        self.master.title("RSS Reader - Eventually")
        top=self.winfo_toplevel()
        """Display the main window"
        with a little bit of padding"""
        self.grid(padx=15, pady=15,sticky=N+S+E+W)
        self.InitResizing()
        self.CreateWidgets()
        
        self.lstSites = []
        self.lstItems = []
        
    def InitResizing(self):
        """Initialize the Resizing of the Window"""
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(6, weight=1)
       
    def CreateWidgets(self):
        """Create all the widgests that we need"""
                       
        """Create the Text"""
        self.lbRSSSiteText = Label(self, text="Select Site:")
        self.lbRSSSiteText.grid(row=0, column=0, sticky=W)
        self.lbRSSItemText = Label(self, text="Select RSS Item:")
        self.lbRSSItemText.grid(row=0, column=6, sticky=W)
        
        """Create the First ListBox"""
        scrollbarV = Scrollbar(self, orient=VERTICAL)
        scrollbarH = Scrollbar(self, orient=HORIZONTAL)
        
        self.lbSites = Listbox(self, selectmode=BROWSE
                                , yscrollcommand=scrollbarV.set
                                , xscrollcommand=scrollbarH.set
                                , relief=SUNKEN)
        self.lbSites.grid(row=1, column=0, columnspan=4, sticky=N+W+S+E)
        """Show the scrollbars and attatch them"""
        scrollbarV.grid(row=1, column=4, sticky=N+S)
        scrollbarV.config(command=self.lbSites.yview)
        scrollbarH.grid(row=2, column=0, columnspan=4, sticky=E+W)
        scrollbarH.config(command=self.lbSites.xview)
        """Set the command"""
        self.lbSites.bind("<Double-Button-1>", self.DblCLickSites)
        
        """Create the Add, Remove, Edit, and View Buttons"""
        self.btnAdd = Button(self, text="Add", command=self.AddRSSItem)
        self.btnAdd.grid(column=0, row=3, stick=E, pady=5)
        self.btnRemove = Button(self, text="Remove", command=self.Display)
        self.btnRemove.grid(column=1, row=3, stick=E, pady=5)
        self.btnEdit = Button(self, text="Edit", command=self.EditRSSItem)
        self.btnEdit.grid(column=2, row=3, stick=E, pady=5)
        self.btnView = Button(self, text="View", command=self.ViewRSSItems)
        self.btnView.grid(column=3, row=3, stick=E, pady=5)
        
        """Create a frame for space between the two items"""
        spaceframe = Frame(self, width=15)
        spaceframe.grid(row=3,column=5)
        
        """Create the Second ListBox"""
        scrollbarV = Scrollbar(self, orient=VERTICAL)
        scrollbarH = Scrollbar(self, orient=HORIZONTAL)
        
        self.lbRSSItems = Listbox(self, selectmode=BROWSE
                                , yscrollcommand=scrollbarV.set
                                , xscrollcommand=scrollbarH.set
                                , relief=SUNKEN)
        self.lbRSSItems.grid(row=1, column=6, sticky=N+W+S+E)
        """Show the scrollbars and attatch them"""
        scrollbarV.grid(row=1, column=7, sticky=N+S)
        scrollbarV.config(command=self.lbRSSItems.yview)
        scrollbarH.grid(row=2, column=6, sticky=E+W)
        scrollbarH.config(command=self.lbRSSItems.xview)
        
        """Create the Frame for space between the ListBoxes and
        the Text"""
        spaceframe = Frame(self, height=5)
        spaceframe.grid(row=4,column=1)
        
        """Create the Text Widget"""
        scrollbarV = Scrollbar(self, orient=VERTICAL)
        scrollbarH = Scrollbar(self, orient=HORIZONTAL)
        self.txtItem = Text(self, wrap=WORD
                             , yscrollcommand=scrollbarV.set
                             , xscrollcommand=scrollbarH.set
                             , relief=SUNKEN
                             , takefocus=0
                             , borderwidth=1
                             , state=NORMAL
                             , cursor="arrow")
        self.txtItem.grid(row=5, column=0
                           , columnspan=7, sticky=N+W+S+E)
        """Show the scrollbars and attatch them"""
        scrollbarV.grid(row=5, column=7, sticky=N+S)
        scrollbarV.config(command=self.txtItem.yview)
        scrollbarH.grid(row=6, column=0, columnspan=7, sticky=E+W)
        scrollbarH.config(command=self.txtItem.xview)
        
        self.txtItem.tag_config("a", foreground="blue", underline=1)
        self.txtItem.tag_bind("a", "<Enter>", self.show_hand_cursor)
        self.txtItem.tag_bind("a", "<Leave>", self.show_arrow_cursor)
        self.txtItem.tag_bind("a", "<Button-1>", self.ClickText)
        self.txtItem.config(cursor="arrow")
        self.txtItem.config(state=DISABLED)
               
        """Create the Set TextButton"""
        self.btnSetText = Button(self, text="SetText", command=self.SetStoryText)
        self.btnSetText.grid(column=6, row=3, stick=E, pady=5)
        
    def show_hand_cursor(self, event):
        event.widget.configure(cursor="hand1")
    def show_arrow_cursor(self, event):
        event.widget.configure(cursor="arrow") 
            
    def DblCLickSites(self, event):
        """Called when lbSites is double-clicked on"
        event containts the x and y position of the click, but since
        we only care about the current selection we can ignore it"""
        self.Display()
        
    def ClickText(self, event):
        """Called when hypelink text is clicked on in the Text Widget
        event contians event information but since
        we only care about the current selection we can ignore it"""
        self.SetStoryText()
        
    def Display(self):
        """Called when btnDisplay is clicked, displays the contents of self.enText"""
        lstCurrSel = self.lbSites.curselection();
        strSelection = "";
        
        if (len(lstCurrSel)==0):
            strSelection = "Nothing yet!"
        else:
            strSelection = self.lbSites.get(lstCurrSel)
        tkMessageBox.showinfo("Text", "You selected: %s" % strSelection)
    
    def SetStoryText(self):
        """Set the Story text, called form the btnSetText""" 
        """Get the Current selection"""
        lstCurrSel = self.lbRSSItems.curselection();
                   
        if (len(lstCurrSel)>0):
            rss_item = self.lstItems[int(lstCurrSel[0])]
            """Set the Text Widgets text"""
            self.txtItem.config(state=NORMAL)
            self.txtItem.delete(1.0,END)
            self.txtItem.insert(INSERT, rss_item.description + "\r\n\r\n")
            self.txtItem.insert(INSERT, rss_item.link, "a")
            self.txtItem.config(state=DISABLED)
        
    def AddRSSItem(self):
        """Add an RSSItem"""
        
        RSSDlg = RSSItemDialog(self.master,"Add new Item")
        if (RSSDlg.Result):
            newSite = RSSSite(RSSDlg.RSSName
                               , RSSDlg.RSSUrl)
            self.lbSites.insert(END, RSSDlg.RSSName)
            self.lbSites.select_clear(0,END)
            self.lbSites.select_set(END)
            self.lstSites.append(newSite)
            
    
    def EditRSSItem(self):
        """Edit an RSSItem"""  
        """Get the Current selection"""
        lstCurrSel = self.lbSites.curselection();
                   
        if (len(lstCurrSel)>0):
            selected_site = self.lstSites[int(lstCurrSel[0])]
            RSSDlg = RSSItemDialog(self
                                    ,"Edit"
                                    , selected_site.Name
                                    , selected_site.Url)
            if (RSSDlg.Result):
                """Update the ListBox"""
                self.lbSites.delete(lstCurrSel)
                self.lbSites.insert(lstCurrSel, RSSDlg.RSSName)
                self.lbSites.select_clear(0,END)
                self.lbSites.select_set(lstCurrSel)
                
                """Save the values in the list"""
                self.lstSites[int(lstCurrSel[0])] =  RSSSite(RSSDlg.RSSName
                               , RSSDlg.RSSUrl)
    def ViewRSSItems(self):
        """Get the Current selection"""
        lstCurrSel = self.lbSites.curselection();
                   
        if (len(lstCurrSel)>0):
            selected_site = self.lstSites[int(lstCurrSel[0])]
            """Empty the ListBox"""
            self.lbRSSItems.delete(0, END)
            rss_reader = RSSReader(selected_site.Url)
            for rss_item in rss_reader.GetItems():
                if (rss_item):
                    self.lbRSSItems.insert(END,rss_item.title)
                    self.lstItems.append(rss_item)
                
if __name__ == "__main__":
    guiFrame = GUIFramework()
    guiFrame.mainloop()