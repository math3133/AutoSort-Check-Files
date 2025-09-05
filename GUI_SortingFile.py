import tkinter as tk
from tkinter.filedialog import askdirectory



class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sorting Files")
        self.resizable(False,True)
        self.geometry("450x600")

        ## Weight expand for frames
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)

        ## Frames instances
        self.FilesOrigin = FolderPath(self, "Select Origin Folder")
        self.FilesOrigin.grid(column=0, row=0, sticky="ew", padx=10, pady=5)

        self.FolderAim = FolderPath(self, "Select Aim Folder")
        self.FolderAim.grid(column=0, row=1, sticky="ew", padx=10, pady=5)

        ## Frame for Feedback when program is executing
        self.FeedbackFrame = tk.Frame(self)
        self.FeedbackFrame.grid(column=0, row=2, sticky="nsew", padx=10, pady=5)
        self.FeedbackFrame.columnconfigure(0, weight=1)
        self.FeedbackFrame.columnconfigure(1, weight=1)
        self.FeedbackFrame.rowconfigure(0, weight=1)
        self.FeedbackFrame.rowconfigure(1, weight=0)

        self.FeedbackListbox = tk.Listbox(self.FeedbackFrame)
        self.FeedbackListbox.grid(column=0, row=0, columnspan=2, sticky="nsew")

        self.FeedbackClear = tk.Button(self.FeedbackFrame, text="Clear Log", command=self.ClearLogs)
        self.FeedbackClear.grid(column=0, row=1, sticky="e", padx=5)

        self.ExecButton = tk.Button(self.FeedbackFrame, text="Organise Files")
        self.ExecButton.grid(column=1, row=1, sticky="w", padx=5)
    
    def ClearLogs(self):
        self.FeedbackListbox.delete(0, tk.END)


## Frame for directory path 
class FolderPath(tk.Frame):
    def __init__(self, parent, ButtonText : str):
        super().__init__(parent)

        ## Weight expand for objects in frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=1)

        self.path = tk.Entry(self)
        self.path.grid(column=0, row=0, sticky="ew")

        self.selectfolder = tk.Button(self, text=ButtonText, command=self.GetFolderPath)
        self.selectfolder.grid(column=1, row=0)

    ## Get folder path from button and register it in variable
    def GetFolderPath(self):
        self.FolderPath = askdirectory()
        self.path.delete(0,tk.END)
        self.path.insert(0, self.FolderPath)




Application().mainloop()