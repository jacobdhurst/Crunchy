# entry_widget.py
from tkinter import *
import time
import Filter
import ProxyTest

root = Tk()

# Create single line text entry box
entry = Text(root, height=10, width=50)
entry.pack()

# Insert some default text
entry.insert(INSERT, '')

# Print the contents of entry widget to console
def print_content():
    unfiltered = open("ProxyList.txt", "w+")
    print("Opened resources/ProxyList.txt")
    unfiltered.write(entry.get("1.0", END))
    print("Wrote to resources/ProxyList.txt")
    unfiltered.close()
    time.sleep(1)
    print("Filtering resources/ProxyList.txt")
    # Filter.main()
    print("resources/FilteredProxyList.txt created")
    time.sleep(1)
    print("Running proxy tests")
    ProxyTest.main()
    print("Proxy test complete")

# Create a button that will print the contents of the entry
button = Button(root, text='Filter', command=print_content)
button.pack()

root.mainloop()
