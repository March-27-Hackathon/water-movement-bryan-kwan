import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.msg = tk.Button(self)
        self.msg["text"] = "Hey Click \nThis Button"
        self.msg["command"] = self.hello
        self.msg.pack(side="top")

        self.quit = tk.Button(self, text = "QUIT", fg = "red", command = self.master.destroy)
        self.quit.pack(side = "bottom")

    def hello(self):
        print("Hiya")

root = tk.Tk()
app = App(master=root)
app.mainloop()
