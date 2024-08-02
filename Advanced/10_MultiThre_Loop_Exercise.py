import threading
import time


def sleep(i):
    print(f'Thread {i} will sleep')
    time.sleep(5)
    print(f'Thread {i} is awake')


for i in range(10):
    th = threading.Thread(target=sleep, args=(i, ))
    th.start()
print('Current thread: ', threading.active_count())
th.join()
print('Current thread: ', threading.active_count())
