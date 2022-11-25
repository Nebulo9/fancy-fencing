from time import sleep
from threading import Thread


def task():
    for i in range(5):
        sleep(1)
        print(i)
    print('done')


# create two new threads
t1 = Thread(target=task)
t2 = Thread(target=task)

# start the threads
# Parallel
t1.start()
t2.start()

t1.join()
t2.join()
# Non parallel
# t1.run()
# t2.run()