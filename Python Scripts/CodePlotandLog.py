import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.ticker as mticker
from scipy.interpolate import make_interp_spline
import serial
import csv
import time
import datetime as dt
arduino = serial.Serial(port='COM8', baudrate=115200,timeout=0)
fileName=["Data"] #name of the CSV file generated
t=0
a = dt.datetime.now()
big_data_x = [[0 for j in range(1)] for i in range(12)]
time_data = []
left_plots=[]
center_plots=[]
right_plots=[]
saved=[]
max_t=int(input("Enter Time range:"));
receive = True
fig = plt.figure(layout='constrained', figsize=(10, 6))
subfigs = fig.subfigures(1, 3, wspace=0.07)
axsLeft = subfigs[0].subplots(6, sharex=True)
subfigs[0].suptitle('Temperature', fontsize='x-large')
subfigs[0].set_facecolor('0.75')
axscenter = subfigs[1].subplots(4, sharex=True)
subfigs[1].set_facecolor('0.85')
subfigs[1].suptitle('Vibration', fontsize='x-large')
axsright=subfigs[2].subplots(1)
subfigs[2].suptitle('Piezo', fontsize='x-large')
subfigs[2].set_facecolor('0.9')

m=0
for ax in axsLeft:
        if m<4:
            left_plots.append(ax.plot([],[],'r-')[0])
        else:
            left_plots.append(ax.plot([],[],'b-')[0])
        m+=1
for ax in axscenter:
        center_plots.append(ax.plot([],[],'g-')[0])
rightfig=axsright.plot([],[],'g-')
    
def WriteNew(fileName):
    global saved
    fileName=fileName+str(dt.datetime.now().strftime('%H-%M-%S'))+".csv"
    print("Here\n")
    print(saved)
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Time(s)","Cylinder 1","Cylinder 2","Cylinder 3","Cylinder 4","Water Outlet","Water Inlet","V1","V2","V3","V4","Piezo"])
        writer.writerows(saved)
    f.close()

def animate(i,big_data_x,time_data,arduino):
    global fig,anim,axsLeft,axscenter,axsright,key,saved,receive,t,left_plots,right,rightfig,a
    try:
        arduino.write(b'g')
        data = arduino.readline()
        d = dt.datetime.now()
        delta=d-a
        print("Time between",t,"--",t-1,"= ",int(delta.total_seconds() * 1000))
        a = dt.datetime.now()
    
        if data:    
            x = (data.decode('utf-8')).split("|")
            if t<max_t :
                if len(x)>8:   
                    
                    if t==0:
                        for i in range(0,11):
                            big_data_x[i][0]=float(x[i])
                    else:
                        for i in range(0,11):
                            if(abs(float(x[i])-big_data_x[i][-1]) > 13) and i < 10:
                               big_data_x[i].append(big_data_x[i][-1])
                               print("Eliminated S:",i,"= ",float(x[i]))
                               x[i]=big_data_x[i][-1]
                            else:
                                big_data_x[i].append(float(x[i]))
                    temp=[]
                    temp.append(t)
                    temp.extend( x[:11])
                    saved.append(temp)
                    time_data.append(t)
                    ##################plot######
                    j=0
                    for ax in left_plots:
                        ax.set_data(time_data,big_data_x[j])
                        axsLeft[j].relim()        # Recalculate limits
                        axsLeft[j].autoscale() #Autoscale
                        j+=1
                    f=0
                    for ax in center_plots:
                        ax.set_data(time_data,big_data_x[f+6])
                        axscenter[f].relim()        # Recalculate limits
                        axscenter[f].autoscale() #Autoscale
                        f+=1
                    
                    rightfig[0].set_data(time_data,big_data_x[10])
                    axsright.relim()        # Recalculate limits
                    axsright.autoscale() #Autoscale
                    axsLeft[0].set_title("Cylinder 1", fontsize='medium')
                    axsLeft[1].set_title("Cylinder 2", fontsize='medium')
                    axsLeft[2].set_title("Cylinder 3", fontsize='medium')
                    axsLeft[3].set_title("Cylinder 4", fontsize='medium')
                    axsLeft[4].set_title("Water Outlet", fontsize='medium')
                    axsLeft[5].set_title("Water Inlet", fontsize='medium')
                    t+=1
                    print(t)
                else:
                    print("hey")
                    print(data.decode('utf-8'))
            elif t==max_t:
                 WriteNew(fileName[0])
                 print("Data Saved");
                 anim.event_source.stop()
                 t+=1
        else:
            print("hey2")
            print(data.decode('utf-8'))
            
             
    except Exception as e:
         print(e)
         e=str(e)
         if ("Write" in e) or ("Serial" in e):
             print("Saving Interupt")
             t=max_t
             WriteNew(fileName[0])
             print("Data Saved");
             anim.event_source.stop()
             t+=1
         pass

fig.suptitle('Sensors Data', fontsize='xx-large')
arduino.flushInput()
arduino.flushOutput()
arduino.flush()
anim = animation.FuncAnimation(fig, animate, fargs=(big_data_x, time_data,arduino),interval=1000)
plt.show()
