import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from collections import deque
import sys 

def main():
    argvs = sys.argv 
    f = open(argvs[1])

    # get acceleration Data
    array = f.read()
    array = array.replace("\r\n",',').split(',')
    array.pop()
    array = map(float,array)

    # Initialize
    accelaration = np.array([array[::4],array[1::4],array[2::4]] )
    gravity = np.array([get_gravity(i[:300]) for i in accelaration])
    linear_accelaration = np.array([[calibration(g,i) for i in list ]for list,g in zip(accelaration,gravity)])
    
    return accelaration,linear_accelaration

def calibration(gravity,accelaration):
    alpha = 0.8
    gravity = alpha * gravity +(1 - alpha) * accelaration
    linear_accelaration = accelaration - gravity
    return linear_accelaration


    

def get_gravity(sample):
    cal_data = reduce(lambda x,y:x + y,sample)/len(sample)
    return cal_data

if __name__ == '__main__':
    accelaration, linear_accelaration = main()

    plt.hold(True)
    plt.ylim([-15,15])
    plt.subplot(621)
    plt.plot(accelaration [0] ,'b')
    plt.ylim([-15,15])
    plt.subplot(623)
    plt.plot(accelaration [1] ,'b')
    plt.ylim([-15,15])
    plt.subplot(625)
    plt.plot(accelaration [2] ,'g')
    plt.ylim([-15,15])

    plt.ylim([-15,15])
    plt.subplot(622)
    plt.plot(linear_accelaration [0] ,'b')
    plt.ylim([-15,15])
    plt.subplot(624)
    plt.plot(linear_accelaration [1] ,'b')
    plt.ylim([-15,15])
    plt.subplot(626)
    plt.plot(linear_accelaration [2] ,'g')
    plt.ylim([-15,15])
    plt.show()


