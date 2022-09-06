import threading
import time

def f1():
    print threading.currentThread().getName()

def f2():
    print threading.current_thread().getName()

def f3():
    print threading.current_thread().getName()


t1 = threading.Thread(target=f1) # use default name
t2 = threading.Thread(name='f2', target=f2)
t3 = threading.Thread(name='f3', target=f3)

t1.start()
t2.start()
t3.start()