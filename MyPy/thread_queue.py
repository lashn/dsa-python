from threading import Thread
import time
import logging
import random
import Queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )

# BUF_SIZE = 5
q = Queue.Queue()


class ThreadCl(Thread):
    def __init__(self, group=None, target=None, name=None,args=(), kwargs=None, verbose=None):
        # group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None
        super(ThreadCl, self).__init__()
        # self.target = target
        # self.name = name

class ProducerThread(ThreadCl):
    def __init__():
        # group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            if not q.full():
                item = random.randint(1, 10)
                q.put(item)
                logging.debug('Putting ' + str(item)
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(random.random())
            else:
                print("queue is full")
        return


# class ConsumerThread(threading.Thread):
#     def __init__(self, group=None, target=None, name=None,
#                  args=(), kwargs=None, verbose=None):
#         super(ConsumerThread, self).__init__()
#         self.target = target
#         self.name = name
#         return
#
#     def run(self):
#         while True:
#             if not q.empty():
#                 item = q.get()
#                 logging.debug('Getting ' + str(item)
#                               + ' : ' + str(q.qsize()) + ' items in queue')
#                 time.sleep(random.randint(1, 10))
#         return


if __name__ == '__main__':
    p = ProducerThread()
    c = ConsumerThread(name='consumer')

    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)