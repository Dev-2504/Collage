import tkinter

def show_text():
    # Entry field માંથી text લઈએ
    user_text = entry_field.get()
    # લેબલ નું text change કરીએ
    my_label.config(text=f"You typed: {user_text}")

# window create
root = tkinter.Tk()
root.title("Entry Field Example")
root.geometry("300x200")

# Entry field create
entry_field = tkinter.Entry(root, width=20)
entry_field.pack(pady=10)

# Button create
my_button = tkinter.Button(root, text="Show Text", command=show_text)
my_button.pack(pady=10)

# Label create
my_label = tkinter.Label(root, text="Type something and click the button")
my_label.pack(pady=10)

# mainloop start
root.mainloop()

# =====================================================================================

# Small Code


import tkinter

# window create
root = tkinter.Tk()
root.title("Only Entry Field")
root.geometry("300x200")

# Entry field create
entry_field = tkinter.Entry(root, width=20)
entry_field.pack(pady=20)

# mainloop start
root.mainloop()
