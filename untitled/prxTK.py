from Tkinter import *
import Queue
import threading
import urllib2
import time

root = Tk()


label1 = Label( root, text="Input Prxy")
E1 = Entry(root, bd =5, width = 50)




def getDate():
    print E1.get()

    myList = E1.get()
    openfile = open("myProxyList.txt", 'w')

    openfile.write(myList)
    openfile.close()





submit = Button(root, text ="Submit", command = getDate)

label1.pack()
E1.pack()





input_file = 'myProxyList.txt'
threads = 10

queue = Queue.Queue()
output = []

class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            #grabs host from queue
            proxy_info = self.queue.get()

            try:
                proxy_handler = urllib2.ProxyHandler({'http':proxy_info})
                opener = urllib2.build_opener(proxy_handler)
                opener.addheaders = [('User-agent','Mozilla/5.0')]
                urllib2.install_opener(opener)
                req = urllib2.Request("http://www.google.com")
                sock=urllib2.urlopen(req, timeout= 7)
                rs = sock.read(1000)
                if '<title>Google</title>' in rs:
                    output.append(('working',proxy_info))
                else:
                    raise "Not Google"
            except:
                output.append(('not working',proxy_info))
            #signals to queue job is done
            self.queue.task_done()

start = time.time()
def main():

    #spawn a pool of threads, and pass them queue instance
    for i in range(5):
        t = ThreadUrl(queue)
        t.setDaemon(True)
        t.start()
    hosts = [host.strip() for host in open(input_file).readlines()]
    #populate queue with data
    for host in hosts:
        queue.put(host)

    #wait on the queue until everything has been processed
    queue.join()

main()
for proxy,host in output:
    print proxy,host

# print "Elapsed Time: %s" % (time.time() - start)


t.pack()





submit.pack(side =BOTTOM)
root.mainloop()