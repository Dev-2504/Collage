import tkinter

def my_button_clicked():
    # button click થવાથી label નું text change કરીએ
    my_label.config(text="Button clicked!")

# window create
root = tkinter.Tk()
root.title("My First GUI")
root.geometry("300x200")

# label create (initial text)
my_label = tkinter.Label(root, text="Hello! Click the button below.")
my_label.pack(pady=10)

# button create
my_button = tkinter.Button(root, text="Click Me!", command=my_button_clicked)
my_button.pack(pady=10)

root.mainloop()
