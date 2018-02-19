# from Tkinter import *
# import Queue
# import threading
# import urllib2
# import time
#
# root = Tk()
#
# label1 = Label( root, text="Input Prxy")
# E1 = Entry(root, bd =5, width = 50)
#
# def getDate():
#     print E1.get()
#
#     myList = E1.get()
#     openfile = open("myProxyList.txt", 'w')
#
#     openfile.write(myList)
#     openfile.close()
#
# submit = Button(root, text ="Submit", command = getDate)
#
# label1.pack()
# E1.pack()
#
# input_file = 'myProxyList.txt'
# threads = 10
#
# queue = Queue.Queue()
# output = []
#
# class ThreadUrl(threading.Thread):
#     """Threaded Url Grab"""
#     def __init__(self, queue):
#         threading.Thread.__init__(self)
#         self.queue = queue
#
#     def run(self):
#         while True:
#             #grabs host from queue
#             proxy_info = self.queue.get()
#
#             try:
#                 proxy_handler = urllib2.ProxyHandler({'http':proxy_info})
#                 opener = urllib2.build_opener(proxy_handler)
#                 opener.addheaders = [('User-agent','Mozilla/5.0')]
#                 urllib2.install_opener(opener)
#                 req = urllib2.Request("http://www.google.com")
#                 sock=urllib2.urlopen(req, timeout= 7)
#                 rs = sock.read(1000)
#                 if '<title>Google</title>' in rs:
#                     output.append(('working',proxy_info))
#                 else:
#                     raise "Not Google"
#             except:
#                 output.append(('not working',proxy_info))
#             #signals to queue job is done
#             self.queue.task_done()
#
# start = time.time()
# def main():
#
#     #spawn a pool of threads, and pass them queue instance
#     for i in range(5):
#         t = ThreadUrl(queue)
#         t.setDaemon(True)
#         t.start()
#     hosts = [host.strip() for host in open(input_file).readlines()]
#     #populate queue with data
#     for host in hosts:
#         queue.put(host)
#
#     #wait on the queue until everything has been processed
#     queue.join()
#
# main()
# for proxy,host in output:
#     print proxy,host
#     print "Elapsed Time: %s" % (time.time() - start)
#
# t.pack()
#
# submit.pack(side =BOTTOM)
# root.mainloop()
#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
# import wx
#
# class ProxyTestGUI(wx.Frame):
#     def __init__(self, parent, id, title):
#         wx.Frame.__init__(self, parent, id, title)
#         self.parent = parent
#         self.initialize()
#
#     def initialize(self):
#         sizer = wx.GridBagSizer()
#
#         self.label = wx.StaticText(self, -1, label=u'Label')
#         sizer.Add(self.label, (0, 0), (1, 1), wx.EXPAND)
#
#         self.entry = wx.TextCtrl(self, -1, value=u"IP LIST")
#         sizer.Add(self.entry, (1, 0), (1, 2), wx.EXPAND)
#         self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry)
#
#         button = wx.Button(self, -1, label="Submit")
#         sizer.Add(button, (1, 3))
#         self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button)
#
#         sizer.AddGrowableCol(0)
#         self.SetSizerAndFit(sizer)
#         self.SetSizeHints(-1, self.GetSize().y, -1, self.GetSize().y)
#         self.entry.SetFocus()
#         self.entry.SetSelection(-1, -1)
#         self.Show(True)
#
#     def OnButtonClick(self, event):
#         self.label.SetLabel("List Submitted")
#         self.entry.SetFocus()
#         self.entry.SetSelection(-1, -1)
#
#     def OnPressEnter(self, event):
#         self.label.SetLabel("List Submitted")
#         self.entry.SetFocus()
#         self.entry.SetSelection(-1, -1)
#
# if __name__ == "__main__":
#     app = wx.App()
#     frame = ProxyTestGUI(None, -1, 'Proxy Tester')
#     app.MainLoop()
#
# import sys
#
# from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot
#
#
# class App(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 textbox - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 400
#         self.height = 140
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         # Create textbox
#         self.textbox = QLineEdit(self)
#         self.textbox.move(20, 20)
#         self.textbox.resize(280, 40)
#
#         # Create a button in the window
#         self.button = QPushButton('Show text', self)
#         self.button.move(20, 80)
#
#         # connect button to function on_click
#         self.button.clicked.connect(self.on_click)
#         self.show()
#
#     @pyqtSlot()
#     def on_click(self):
#         textboxValue = self.textbox.text()
#         QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
#                              QMessageBox.Ok)
#         self.textbox.setText("")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())