from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import filedialog

#root=Tk()
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520


    def __init__(self):
        super().__init__()
        window = Tk()

        notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays

        tab1 = Frame(notebook) #new frame for tab 1
        tab2 = Frame(notebook) #new frame for tab 2

        notebook.add(tab1,text="Tab 1")
        notebook.add(tab2,text="Tab 2")
        notebook.pack(expand=True,fill="both")  #expand = expand to fill any space not otherwise used
                                               #fill = fill space on x and y axis
        #Label(tab1,text="Hello, this is tab#1",width=50,height=25).pack()
        #Label(tab2,text="Goodbye, this is tab#2",width=50,height=25).pack()

        self.title("memoryVol")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed



        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="memoryVol",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        #Open File Button
        def open():
            root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", 
                                                        filetypes=(("bin files", "*.bin"), 
                                                                    ("raw files", "*.raw"), 
                                                                    ("bmp files", "*.bmp"), 
                                                                    ("mem files", "*.mem"),
                                                                    ("vmem files", "*.vmem"),("all files", "*.*")))
            File_Lable = Label(root, text = root.filename).pack() 

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="add file", fg_color="green",text_color="#ffffff", command=open)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        #Remove File Button
        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="remove file",
                                                command=self.button_event, 
                                                fg_color="red",
                                                text_color="#ffffff")
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="generate report",
                                                command=self.button_event, 
                                                fg_color="#004d00",
                                                text_color="#ffffff")
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="RUN",
                                                command=self.button_event, 
                                                fg_color="#ff9900",
                                                text_color="#ffffff")
        self.button_4.grid(row=5, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=8, pady=20, padx=20, sticky="nsew")

    

        #============= Text Box  =============

        def button_click_event():
            dialog = customtkinter.CTkInputDialog(master=self, text="Search:", title="Search for a keyword")
            print("Number:", dialog.get_input())


        self.button = customtkinter.CTkButton(master=self, text="Search for a keyword", command=button_click_event)
        #button.place(relx=0.85, rely=0.79, anchor=tkinter.CENTER)
        self.button.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")



        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Select the architecture")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=0, text="Windows", fg_color="green")
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                            variable=self.radio_var,
                                                            value=1, text="Linux_OS", fg_color="green")   
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                            variable=self.radio_var,
                                                            value=2, text="Mac _OS", fg_color="green")
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["Imageinfo", "Kdbgscan", "Processes ","PSlist","PSscan","DLL","DLLList","DLLDump","Handles","Getsids","Netscan","Hivelist","Timeliner","HashDump","Lsadump","Modscan","FileScan","Svcscan","Cmdscan","Iehistory","Dumpregistry","Moddump","Procdump","Memdump"])
        self.combobox_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")


       

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_right,
                                                text="Mutilple Scan")
        self.switch_1.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.combobox_2 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["Imageinfo", "Kdbgscan", "Processes ","PSlist","PSscan","DLL","DLLList","DLLDump","Handles","Getsids","Netscan","Hivelist","Timeliner","HashDump","Lsadump","Modscan","FileScan","Svcscan","Cmdscan","Iehistory","Dumpregistry","Moddump","Procdump","Memdump"])
        self.combobox_2.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_right,
                                                text="Switch 02")
        self.switch_2.grid(row=7, column=2, columnspan=1, pady=10, padx=20, sticky="we")


        self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="CheckBox 01")
        self.check_box_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="CheckBox 02")
        self.check_box_2.grid(row=9, column=1, pady=10, padx=20, sticky="w")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Search For")
        self.entry.grid(row=10, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Search",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_5.grid(row=10, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.optionmenu_1.set("Dark")
        #self.button_3.configure(state="disabled", text="Disabled CTkButton")
        self.combobox_1.set("Type of Scan")
        self.combobox_2.set("Type of Scan")
        self.radio_button_1.select()
        self.switch_2.select()
        #self.radio_button_3.configure(state=tkinter.DISABLED)
        #self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        self.check_box_2.select()

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()