from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from queue import Queue
import threading
import urllib3
import time
import os

input_file = 'filtered.txt'

queue = Queue()
output = []
#
# class ChromeTest():
#     def test(self):
#         input_file = open("filtered.txt", "r")
#         i = 0
#         for proxy in input_file:
#             driverLocation = "C:/Users/Jacob/Documents/chromedriver.exe" #/Users/danielguzman/Documents/workspace/chromedriver"
#             os.environ["webdriver.chrome.driver"] = driverLocation
#
#             options = webdriver.ChromeOptions()
#             options.add_argument('--proxy-server=%s' % proxy)
#             options.add_experimental_option("detach", True)
#             options.set_headless(True)
#
#             driver = webdriver.Chrome(driverLocation, chrome_options=options)
#             driver.get("http://google.com")
#             if not(driver.page_source.__contains__("ERR")): print(i, ":", driver.current_url, " Success:", proxy)
#
#             i = i + 1

class threadTest(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            #grabs host from queue
            proxyToTest = self.queue.get()
            try:
                driverLocation = "C:/Users/Jacob/Documents/chromedriver.exe"  # /Users/danielguzman/Documents/workspace/chromedriver"
                os.environ["webdriver.chrome.driver"] = driverLocation

                options = webdriver.ChromeOptions()
                options.add_argument('--proxy-server=%s' % proxyToTest)
                options.add_experimental_option("detach", True)
                options.set_headless(True)

                driver = webdriver.Chrome(driverLocation, chrome_options=options)
                driver.get("http://google.com")
                if not (driver.page_source.__contains__("ERR")):
                    print ("Success:", proxyToTest)
                    output.append(("Success:", proxyToTest))
                else:
                    raise ("Error.")
            except:
                print ("Failure:", proxyToTest)
                output.append(("Failure:", proxyToTest))
            #signals to queue job is done
            self.queue.task_done()

start = time.clock()
def main():
    # c = ChromeTest()
    # c.test()

    # spawn a pool of threads, and pass them queue instance
    for i in range(50): # 50 threads
        t = threadTest(queue)
        t.setDaemon(True)
        t.start()

    hosts = [host.strip() for host in open(input_file).readlines()]
    # populate queue with data
    for host in hosts:
        queue.put(host)

    # wait on the queue until everything has been processed
    queue.join()


main()
print("Elapsed Time: %lf seconds" % (time.clock() - start))
# for proxyToTest, host in output:
#     print(proxyToTest, host)