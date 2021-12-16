import threading
import time

#track time taken to execute the entire script
start_time = time.perf_counter()

def thread_fuction(seconds):
    print("thread started")
    time.sleep(seconds)
    print("Done sleeping %d seconds" % seconds)

#first thread
t1=threading.Thread(target=thread_fuction,args=[2])
t2=threading.Thread(target=thread_fuction,args=[1])
t1.start()
t2.start()
t1.join()
t2.join()


finish_time = time.perf_counter()
print(f'time take for entire script is {round(finish_time-start_time,2)} ',end='')

