from threading import Thread
import time
import requests


def download(url, name):
    result = requests.get(url)
    f = open(name, "wb")
    f.write(result.content)
    f.close()


urls = [["https://picsum.photos/200/300?grayscale", "1.jpg"],
        ["https://picsum.photos/200/300?grayscale", "2.jpg"],
        ["https://picsum.photos/200/300?grayscale", "3.jpg"],
        ["https://picsum.photos/200/300?grayscale", "4.jpg"],
        ["https://picsum.photos/200/300?grayscale", "5.jpg"]]

start_time = time.time()

threads = []
for url in urls:
# for url, name in urls:
    threads.append(Thread(target=download, args=(url[0], url[1])))
    # threads.append(Thread(target=download, args=(url, name)))

for thread in threads:
    thread.start()
    thread.join()

end_time = time.time()
print(end_time - start_time)
