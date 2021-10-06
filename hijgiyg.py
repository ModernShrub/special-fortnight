from tkinter import*
from tkinter import ttk

root = Tk()
root.geometry("600x600")
root.title("iygweyhw")

ele = ["Label", "Button", "Dropdown"]

selele = StringVar()

drp = ttk.Combobox(root, values = ele, textvariable = selele)
drp.pack()
selelef = selele.get()
print(selelef)

class crel():
    def __init__(self):
        print("Hello")
        
    def crnele(self):
        selelef = selele.get()
        print(selelef)
        
        if selelef == "Label":
            label = Label(root, text="Label")
            label.pack()
            print("done")
            
        if selelef == "Button":
            btn1 = Button(root, text="Button", command=self.msg)
            btn1.pack(padx=10,pady=10)
            print("done")
            
        if selelef == "Dropdown":
            val = ["1", "2", "A", "B", "!", "@"]
            drop = ttk.Combobox(root, values = val, state="readonly")
            drop.pack(padx=10,pady=10)
            print("done")
            
    def msg(self):
        messagebox.showinfo("Message", "New Button clicked")
        
obj = crel()
btn = Button(root, text = "Create Element", command = obj.crnele)
btn.pack(padx=20,pady=20)

root.mainloop()