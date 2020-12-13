# Author: Paul McGuire
import atexit
from time import clock, strftime, localtime
from datetime import timedelta

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def log(s, elapsed=None):
    global laps
    line = "="*40
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        t = clock()
        print("Elapsed time:", "{:.4f}".format((t - laps) * 1000.), " ms")
        laps = t
    print(line)
    print()

def endlog():
    end = clock()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

start = laps =  clock()
atexit.register(endlog)
log("Start Program")