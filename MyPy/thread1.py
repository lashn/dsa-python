import threading


def fun(id,ij):
    print 'thread fun %s %s' %(id, ij)
    return

if __name__=='__main__':
    j=10
    for i in range(3):
        t=threading.Thread(target=fun, args=(i,j))
        t.start()



