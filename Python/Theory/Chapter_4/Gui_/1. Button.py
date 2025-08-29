import tkinter

# નવું function બનાવ્યું
def my_button_clicked():
    print("Button clicked!")

# window create
root = tkinter.Tk()
root.title("My First GUI")
root.geometry("300x200")

# button create
my_button = tkinter.Button(root, text="Click Me!", command=my_button_clicked)

# button ને window માં મૂકીએ
my_button.pack(pady=20)

# mainloop start
root.mainloop()
