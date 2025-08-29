import tkinter
from tkinter import messagebox

def show_dialog():
        
    # 1️⃣ Information dialog
    messagebox.showinfo("Info", "This is an information dialog.")
    
    # 2️⃣ Warning dialog
    messagebox.showwarning("Warning", "This is a warning dialog.")
    
    # 3️⃣ Error dialog
    messagebox.showerror("Error", "This is an error dialog.")
    
    # 4️⃣ Yes/No question dialog
    response = messagebox.askyesno("Question", "Do you want to continue?")
    print(response)  # True if Yes, False if No
    
    # 5️⃣ OK/Cancel dialog
    response = messagebox.askokcancel("Confirm", "Do you want to save?")
    print(response)  # True if OK, False if Cancel



# window create
root = tkinter.Tk()
root.title("Dialog Example")
root.geometry("300x200")

# Button create – click કરવાથી dialog આવશે
my_button = tkinter.Button(root, text="Show Dialog", command=show_dialog)
my_button.pack(pady=50)

# mainloop start
root.mainloop()