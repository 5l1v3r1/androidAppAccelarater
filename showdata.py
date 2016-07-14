import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from collections import deque
import sys

def MovingAverage(data,N = 5):
    queue = deque(data[:N])
    new_data = []

    for i in data:
        new_data.append(reduce(lambda x,y:x+y,queue)/N)
        queue.popleft()
        queue.append(i)

    return new_data

def Calibrate(data,s = 3):
    sample = 3 * 100
    cal_data = reduce(lambda x,y: x + y,data[:sample])/sample

    return cal_data

if __name__ == '__main__':
    argvs = sys.argv
    f = open(argvs[1])
    
    array = f.read()
    array = array.replace("\r\n",',').split(',')
    array.pop()
    array = map(float,array)
    x = array[::4]
    y = array[1::4]
    z = array[2::4]
    
    #c =  map(lambda x,y:x-y,a,x)
    #plt.subplot(313)
    #plt.plot(c)

    x1= MovingAverage(map(lambda f: f - Calibrate(x,3), x),15)
    y1= MovingAverage(map(lambda f: f - Calibrate(y,3), y),15)
    z1= MovingAverage(map(lambda f: f - Calibrate(z,3), z),15)
    
    plt.hold(True)
    plt.ylim([-15,15])
    plt.subplot(321)
    plt.plot(x,'b')
    plt.ylim([-15,15])
    plt.subplot(322)
    plt.plot(x1,'b')
    plt.ylim([-15,15])
    plt.subplot(323)
    plt.plot(y,'g')
    plt.ylim([-15,15])
    plt.subplot(324)
    plt.plot(y1,'g')
    plt.ylim([-15,15])
    plt.subplot(325) 
    plt.plot(z,'k')
    plt.ylim([-15,15])
    plt.subplot(326) 
    plt.plot(z1,'k')
    plt.ylim([-15,15])
    plt.show()
