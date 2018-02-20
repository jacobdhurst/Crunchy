import tkinter as tk  # for python 3
import pygubu


class Application:
    def __init__(self, master):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('ProxyTester.ui')

        #3: Create the widget using a master as parent
        self.root = builder.get_object('root', master)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()