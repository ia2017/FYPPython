from matplotlib import pyplot as plt
import numpy as np


import os, sys
from csv import writer
import pandas as pd

# Function to get number of variables from FFD
def getvariablenumber(file):
    f = open(file,'r')
    # Finding line where FFD Degree is
    i = 0
    for line in f:
        if 'FFD_DEGREE' in line:
            c = i
        i=i+1

    f.seek(0)
    lines = f.readlines()
    #print(lines[c])
    i=0
    deg=1
    temp=''
    for char in lines[c]:
        if char.isdigit() == True:
            temp=temp+char
        elif temp!='' and char.isdigit() == False and temp!='0':
            deg=deg*(int(temp)+1)
            temp=''
        else:
            temp=''

    f.close()
    print("Deg: " + str(deg))
    return deg



# ------- Input parameters ---------
file = 'configunswept.cfg'
partition = 1
quiet = False
nzones = 1
step = 1e-4
compute = True
validate = False
mode = 'all'

# ----- Defining united file ------
f = open('of_grad_compare.csv', 'w', newline='')
csv_writer = writer(f)

# Defining header with design variables
header = []
header.append('DV')
n=getvariablenumber(file)
for i in range(0,n):
    header.append(i)
csv_writer.writerow(header)
f.close()

if os.path.exists('of_grad_fluid_findiff.csv'):
    findiff=pd.read_csv('of_grad_fluid_findiff.csv')
    header = findiff.head(0)
    i = 0
    for head in header:
        if "DRAG" in head:
            d = i
        i=i+1

    findiff=findiff.to_numpy()
    draggrad=findiff[:,d]
    draggrad=draggrad*10e-4
    # Writing to file
    f = open('of_grad_compare.csv', 'a', newline='')
    csv_writer = writer(f)
    draggrad=draggrad.tolist()
    FD=[]
    FD.append('FD')
    for num in draggrad:
        FD.append(num)
    csv_writer.writerow(FD)
    f.close()


# Putting into file
if os.path.exists('of_grad_cd.csv'):
    findiff=pd.read_csv('of_grad_cd.csv')
    header = findiff.head(0)
    i = 0
    for head in header:
        if "GRADIENT" in head:
            d = i
        i=i+1

    findiff=findiff.to_numpy()
    draggrad=findiff[:,d]

    # Writing to file
    f = open('of_grad_compare.csv', 'a', newline='')
    csv_writer = writer(f)
    draggrad=draggrad.tolist()
    FD=[]
    FD.append('Adjoint')
    for num in draggrad:
        FD.append(num)
    csv_writer.writerow(FD)
    f.close()


SIZEPLT = 28
plt.rc('font', size=SIZEPLT)          # controls default text sizes
plt.rc('axes', titlesize=SIZEPLT)     # fontsize of the axes title
plt.rc('axes', labelsize=SIZEPLT)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('legend', fontsize=SIZEPLT)    # legend fontsize
plt.rc('figure', titlesize=SIZEPLT)  # fontsize of the figure title

# ----- Plots -------

f = open('of_grad_compare.csv','r')
lines=f.readlines()
chars=''

charslistfull=[]
charslist=[]
for line in lines:
    for char in line:
        if char == ',' or char == ' ' or char == '\n':
            charslist.append(chars)
            chars=''
        else:
            chars=chars+char
    charslistfull.append(charslist)
    charslist=[]

i=0
DV=[]
for index in charslistfull[0][1:]:
    DV.append(int(index))
    i+=1

i=0
FD=[]
for index in charslistfull[1][1:]:
    FD.append(float(index))
    i += 1

i=0
Adj=[]
for index in charslistfull[2][1:]:
    Adj.append(float(index))
    i += 1

difference=np.zeros(len(DV))
for i in range(0,len(DV)-1):
    difference[i]=abs(FD[i]-Adj[i])

norm=np.linalg.norm(difference)
print('Difference = ' + str(norm))

plt.figure(1,figsize=(20,16))
plt.title('FD vs Adjoint')
plt.plot(DV,FD,label='FD',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(DV,Adj,label='Adjoint',marker='.',linestyle='-',linewidth=2,markersize=20)
plt.xlabel('Design Variable')
plt.ylabel('Drag Gradient')
plt.legend()
plt.xlim(0,len(DV))
plt.grid()
plt.show()

f.close()