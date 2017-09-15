#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017年9月13日

@author: Ethan Wong
'''
import threading
import thread
import time
import Queue

'''gl_num = 0

lock = threading.RLock()

def Func():
    lock.acquire()
    global gl_num
    gl_num +=1
    time.sleep(1)
    print gl_num
    lock.release()
    
for i in range(10):
    t = threading.Thread(target=Func)
    t.start()'''

'''# 为线程定义一个函数
def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % ( threadName,time.ctime(time.time()) )

# 创建两个线程
try:
    thread.start_new_thread( print_time,("Thread-1",1,) )
    thread.start_new_thread( print_time,("Thread-2",2,) )
except:
    print "Error: unable to start thread"
    
while 1:
    pass'''


'''#使用Threading模块创建线程，直接从threading.Thread继承，然后重写__init__方法和run方法：
exitFlag = 0

#继承父类threading.Thread
class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
    def run(self):
        print "Starting " + self.name
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        
        print_time(self.name,self.counter,3)
        #print "Exiting " + self.name
        threadLock.release()
        
    
def print_time(threadName,delay,counter):
    while counter:
        #if exitFlag:
        #    threading.Thread.exit()
        time.sleep(delay)
        print "%s: %s :%s" % (threadName,time.ctime(time.time()),counter)
        counter -= 1

threadLock = threading.Lock()
threads = []

#创建新线程
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

#开启线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)
 
# 等待所有线程完成
for t in threads:
    t.join()
print threads
print "\nExiting Main Thread"

'''
#使用Thread对象的Lock和Rlock可以实现简单的线程同步，
#这两个对象都有acquire方法和release方法，
#对于那些需要每次只允许一个线程操作的数据，
#可以将其操作放到acquire和release方法之间。
exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        #调用process_data函数
        process_data(self.name,self.q)
        print "Exiting " + self.name
        
def process_data(threadName,q):
    while not exitFlag:
        #获得锁 每次只允许一个线程操作的数据、共享数据
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            #释放锁
            queueLock.release()
            print "%s processing %s" % (threadName,data)
        else:
            queueLock.release()
        time.sleep(1)
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

#创建新线程
for tName in threadList:
    thread = myThread(threadID,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
    
#填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

#等待队列清空
while not workQueue.empty():
    pass

#通知线程是时候推出
exitFlag = 1

#等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"

