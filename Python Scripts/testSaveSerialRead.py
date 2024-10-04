import serial
import time
import csv
arduino = serial.Serial(port='COM8', baudrate=115200,timeout=0)
fileName=["Data.csv"] #name of the CSV file generated
saved=[]
t=0;
m=1
temp=[]
def WriteNew(fileName):
    global saved
    print("Here\n")
    print(saved)
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Time(s)","T1","T2","T3","T4","T5","T6","T7","V1","V2","V3","V4","P"])
        #writer.writerows(map(lambda x: [x], savedrows))
        #if(len(saved)>20):
            #writer.writerow(saved[0])
            #writer.writerows(saved[-20:])
        #else:
        writer.writerows(saved)
    f.close()
    #rows = list(csvreader)
    #for x in rows:
x="5"
arduino.flushInput()
arduino.write(x.encode())  
while t<10:
    try:
        
        data = arduino.readline()
        print(data.decode('utf-8'))
        arduino.flushInput()
        x = (data.decode('utf-8')).split("|")
        if len(x)>2:
            temp=[]
            temp.append(t)
            for value in x:
                temp.append(value)
            saved.append(temp)
            t+=1
        time.sleep(1)
    except:
        print("Exception")
        pass
WriteNew(fileName[0])
print("Data Saved");
