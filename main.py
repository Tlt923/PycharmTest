import time

import blog_spider
import threading

urls = [f"http://www.cnblogs.com/#p{i+2}" for i in range(50)]


def crawl_single_thread():
    for url in urls:
        blog_spider.crawl_func(url)

def crawl_multi_thread():

    threads = []

    for url in urls:
        thread = threading.Thread(target=blog_spider.crawl_func, args=(url,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    start_time = time.time()
    crawl_single_thread()
    end_time = time.time()
    print(end_time-start_time)

    start_time = time.time()
    crawl_multi_thread()
    end_time = time.time()
    print(end_time - start_time)

