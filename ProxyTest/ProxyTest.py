from queue import Queue
import urllib3
import threading
import time


input_file = 'filtered.txt'
threads = 10

queue = Queue()
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
                proxy_handler = urllib3.ProxyHandler({'http':proxy_info})
                opener = urllib3.build_opener(proxy_handler)
                opener.addheaders = [('User-agent','Mozilla/5.0')]
                urllib3.install_opener(opener)
                req = urllib3.request("https://www.google.com")
                sock=urllib3.urlopen(req, timeout=120)
                rs = sock.read(1000)
                if '<title>Google</title>' in rs:
                    output.append(('Working:',proxy_info))
                else:
                    raise ("Error: Not Google.")
            except:
                output.append(('Not Working:',proxy_info))
            #signals to queue job is done
            self.queue.task_done()

start = time.clock()
def main():
    # spawn a pool of threads, and pass them queue instance
    for i in range(5):
        t = ThreadUrl(queue)
        t.setDaemon(True)
        t.start()
    hosts = [host.strip() for host in open(input_file).readlines()]
    # populate queue with data
    for host in hosts:
        queue.put(host)

    # wait on the queue until everything has been processed
    queue.join()


main()
for proxy, host in output:
    print(proxy, host)

print("Elapsed Time: %lf seconds" % (time.clock() - start))