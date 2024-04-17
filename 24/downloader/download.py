from threading import Thread
from multiprocessing import Process
from queue import Queue
import time
import requests


def download(url, name):
    result = requests.get(url)
    # my_queue.put(result.text)
    f = open(name, "wb")
    f.write(result.content)
    f.close()


urls = [["https://picsum.photos/200/300?grayscale", "1.jpg"],
        ["https://picsum.photos/200/300?grayscale", "2.jpg"],
        ["https://picsum.photos/200/300?grayscale", "3.jpg"],
        ["https://picsum.photos/200/300?grayscale", "4.jpg"],
        ["https://picsum.photos/200/300?grayscale", "5.jpg"]]

start_time = time.time()
# my_queue = Queue()
threads = []
for url in urls:
    # direct access to elements
    # for url, name in urls:
    # threads.append(Thread(target=download, args=(url, name)))
    threads.append(Thread(target=download, args=(url[0], url[1])))
    # if you want to use process instead of thread
    # threads.append(Process(target=download, args=(url[0], url[1])))
for thread in threads:
    thread.start()
    thread.join()

# while not my_queue.empty():
#     print(my_queue.get())

end_time = time.time()
print(end_time - start_time)
