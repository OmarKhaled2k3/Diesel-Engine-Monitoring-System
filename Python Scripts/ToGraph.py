import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import numpy as np
import csv
from pandas import *

# Create figure for plotting
fig = plt.figure(layout='constrained', figsize=(10, 6))
subfigs = fig.subfigures(1, 2, wspace=0.07)
axsLeft = subfigs[0].subplots(6, sharex=True)
subfigs[0].suptitle('Temperature', fontsize='x-large')
subfigs[0].set_facecolor('0.75')
axscenter = subfigs[1].subplots(4, sharex=True)
subfigs[1].set_facecolor('0.85')
subfigs[1].suptitle('Vibration', fontsize='x-large')
m=0
for ax in axsLeft:
        if m<4:
            ax.plot([],[],'r-')
        else:
            ax.plot([],[],'b-')
        m+=1
for ax in axscenter:
        ax.plot([],[],'g-')

filename=input("Enter Filename:")
filename+=".csv"
def Plotlog(fileName,ax):
    time=[]
    newy=[]
    data=read_csv(fileName)
    c1 = data['Cylinder 1'].tolist()
    c2 = data['Cylinder 2'].tolist()
    c3 = data['Cylinder 3'].tolist()
    c4 = data['Cylinder 4'].tolist()
    wo = data['Water Outlet'].tolist()
    wi = data['Water Inlet'].tolist()
    wi = data['Water Inlet'].tolist()
    v1 = data['V1'].tolist()
    v2 = data['V2'].tolist()
    v3 = data['V3'].tolist()
    v4 = data['V4'].tolist()
    big_data_x=[c1,c2,c3,c4,wo,wi,v1,v2,v3,v4]
    time_data = data['Time(s)'].tolist()
    j=0
    for ax in axsLeft:
        if j<4:
            ax.plot(time_data,big_data_x[j],'r-')
        else:
            ax.plot(time_data,big_data_x[j],'b-')
        j+=1
    f=0
    for ax in axscenter:
        ax.plot(time_data,big_data_x[f+6],'g-')
        f+=1

    axsLeft[0].set_title("Cylinder 1", fontsize='medium')
    axsLeft[1].set_title("Cylinder 2", fontsize='medium')
    axsLeft[2].set_title("Cylinder 3", fontsize='medium')
    axsLeft[3].set_title("Cylinder 4", fontsize='medium')
    axsLeft[4].set_title("Water Outlet", fontsize='medium')
    axsLeft[5].set_title("Water Inlet", fontsize='medium')

Plotlog(filename,axsLeft)
plt.show()
