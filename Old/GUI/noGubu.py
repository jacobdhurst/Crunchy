# entry_widget.py
from tkinter import *
from ProxyTest import Filter

root = Tk()

# Create single line text entry box
entry = Entry(root)
entry.pack()

# Insert some default text
entry.insert(INSERT, 'Hewwo???')

# Print the contents of entry widget to console
def print_content():
    unfiltered = open("../ProxyTest/ProxyList.txt", "a+")
    print("Opened unfiltered.txt")
    unfiltered.write(entry.get())
    print("Wrote to unfiltered.txt")
    Filter.execute(unfiltered)


# Create a button that will print the contents of the entry
button = Button(root, text='Test', command=print_content)
button.pack()

root.mainloop()