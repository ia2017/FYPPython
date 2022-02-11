import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Extracting Data

# Optimization
f1=open('generalfixedcl.pbs.o3074123','r')
lines1=f1.readlines()[39:69]
f1.close()
f2=open('generalcladj.o3077839','r')
lines2=f2.readlines()[41:71]
f2.close()

nit1=[]
fc1=[]
obj1=[]
gnorm1=[]

for line in lines1:
    num = ''
    i=0
    prevspace = True
    if line[4].isdigit()==True:
        for char in line:
            if char == ' ' and prevspace == False:
                if i==0:
                    nit1.append(float(num))
                elif i==1:
                    fc1.append(float(num))
                elif i == 2:
                    obj1.append(float(num))
                i+=1
                num=''
                prevspace = True
            elif char.isdigit() == True or char == '.' or char =='-' or char=='E':
                num = num + char
                prevspace = False
        gnorm1.append(float(num))

print(lines2)

nit2=[]
fc2=[]
obj2=[]
gnorm2=[]

for line in lines2:
    num = ''
    i=0
    prevspace = True
    if line[4].isdigit()==True:
        for char in line:
            if char == ' ' and prevspace == False:
                if i==0:
                    nit2.append(float(num))
                elif i==1:
                    fc2.append(float(num))
                elif i == 2:
                    obj2.append(float(num))
                i+=1
                num=''
                prevspace = True
            elif char.isdigit() == True or char == '.' or char =='-' or char=='E':
                num = num + char
                prevspace = False
        gnorm2.append(float(num))

# CL and CD

history1=pd.read_csv('history_project_fixedcl.csv')
history2=pd.read_csv('history_project_cladj.csv')

history1.columns=history1.columns.str.replace('"','')
history2.columns=history2.columns.str.replace('"','')
eval1=history1['EVALUATION    ']
eval2=history2['EVALUATION    ']
cl1=history1[' LIFT          ']
cd1=history1[' DRAG          ']
cl2=history2[' LIFT          ']
cd2=history2[' DRAG          ']


# ---- Plots ------
SIZEPLT = 28
plt.rc('font', size=SIZEPLT)          # controls default text sizes
plt.rc('axes', titlesize=SIZEPLT)     # fontsize of the axes title
plt.rc('axes', labelsize=SIZEPLT)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('legend', fontsize=SIZEPLT)    # legend fontsize
plt.rc('figure', titlesize=SIZEPLT)  # fontsize of the figure title

plt.figure(1,figsize=(20,16),dpi=120)
plt.plot(nit1,obj1,label='Fixed CL',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(nit2,obj2,label='CL > 0.3',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.grid()
plt.legend()
plt.xlabel('Optimization Iteration')
plt.ylabel('Objective Function')

plt.figure(2,figsize=(20,16),dpi=120)
plt.plot(nit1,gnorm1,label='Fixed CL',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(nit2,gnorm2,label='CL > 0.3',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.grid()
plt.legend()
plt.xlabel('Optimization Iteration')
plt.ylabel('GNORM')

plt.figure(3,figsize=(20,16),dpi=120)
plt.plot(eval1,cl1,label='Fixed CL',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(eval2,cl2,label='CL > 0.3',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.grid()
plt.legend()
plt.xlabel('Evaluations')
plt.ylabel('CL')

plt.figure(4,figsize=(20,16),dpi=120)

plt.plot(eval1,cd1,label='Fixed CL',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(eval2,cd2,label='CL > 0.3',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.grid()
plt.legend(loc='best')
plt.xlabel('Evaluations')
plt.ylabel('CD')

plt.show()
