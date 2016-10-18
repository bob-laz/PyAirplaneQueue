import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)


def print_event(name):
    print("Event: " + str(time.time()) + " " + name)



print('START:' + str(time.time()))
scheduler.enter(2, 1, print_event, ('first',))
scheduler.enter(3, 1, print_event, ('second',))

scheduler.run()
