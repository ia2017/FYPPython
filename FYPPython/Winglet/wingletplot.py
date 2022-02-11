import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Extracting Data

# Optimization
f1=open('generalwingletynormal.pbs.o3080694','r')
lines1=f1.readlines()[39:63]
f1.close()
f2=open('generalwingletnormal.pbs.o3084134','r')
lines2=f2.readlines()[41:71]
f2.close()
f3=open('generalwinglet1ffd.pbs.o3080692','r')
lines3=f3.readlines()[41:71]
f3.close()
f4=open('generalcoupled3.pbs.o3129613','r')
lines4=f4.readlines()[38:49]


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

nit3=[]
fc3=[]
obj3=[]
gnorm3=[]

for line in lines3:
    num = ''
    i=0
    prevspace = True
    if line[4].isdigit()==True:
        for char in line:
            if char == ' ' and prevspace == False:
                if i==0:
                    nit3.append(float(num))
                elif i==1:
                    fc3.append(float(num))
                elif i == 2:
                    obj3.append(float(num))
                i+=1
                num=''
                prevspace = True
            elif char.isdigit() == True or char == '.' or char =='-' or char=='E':
                num = num + char
                prevspace = False
        gnorm3.append(float(num))

nit4=[]
fc4=[]
obj4=[]
gnorm4=[]

for line in lines3:
    num = ''
    i=0
    prevspace = True
    if line[4].isdigit()==True:
        for char in line:
            if char == ' ' and prevspace == False:
                if i==0:
                    nit4.append(float(num))
                elif i==1:
                    fc4.append(float(num))
                elif i == 2:
                    obj4.append(float(num))
                i+=1
                num=''
                prevspace = True
            elif char.isdigit() == True or char == '.' or char =='-' or char=='E':
                num = num + char
                prevspace = False
        gnorm4.append(float(num))
# CL and CD

history1=pd.read_csv('history_project_ynormal.csv')
history2=pd.read_csv('history_project_wingletnormal.csv')
history3=pd.read_csv('history_project_1ffd.csv')
history4=pd.read_csv('history_project_coupled.csv')

history1.columns=history1.columns.str.replace('"','')
history2.columns=history2.columns.str.replace('"','')
history3.columns=history3.columns.str.replace('"','')
history4.columns=history4.columns.str.replace('"','')
eval1=history1['EVALUATION    ']
eval2=history2['EVALUATION    ']
eval3=history3['EVALUATION    ']
cl1=history1[' LIFT          ']
cd1=history1[' DRAG          ']
cl2=history2[' LIFT          ']
cd2=history2[' DRAG          ']
cl3=history3[' LIFT          ']
cd3=history3[' DRAG          ']
eval4=history4['EVALUATION    ']
cl4=history4[' LIFT          ']
cd4=history4[' DRAG          ']

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
plt.plot(nit1,obj1,label='Y Normal',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(nit2,obj2,label='Winglet Normal',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(nit3,obj3,label='1 FFD box',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.grid()
plt.legend()
plt.xlabel('Optimization Iteration')
plt.ylabel('Objective Function')

plt.figure(2,figsize=(20,16),dpi=120)
plt.plot(nit1,gnorm1,label='Y Normal',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(nit2,gnorm2,label='Winglet Normal',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(nit3,gnorm3,label='1 FFD box',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.grid()
plt.legend()
plt.xlabel('Optimization Iteration')
plt.ylabel('GNORM')

plt.figure(3,figsize=(20,16),dpi=120)
plt.plot(eval1,cl1,label='Y Normal',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(eval2,cl2,label='Winglet Normal',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(eval3,cl3,label='1 FFD box',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.grid()
plt.legend()
plt.xlabel('Evaluations')
plt.ylabel('CL')

plt.figure(4,figsize=(20,16),dpi=120)

plt.plot(eval1,cd1,label='Y Normal',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(eval2,cd2,label='Winglet Normal',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.plot(eval3,cd3,label='1 FFD box',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.grid()
plt.legend(loc='right')
plt.xlabel('Evaluations')
plt.ylabel('CD')

# ---- Coupled ----

plt.figure(5,figsize=(20,16),dpi=120)
plt.plot(nit4,obj4,label='Coupled Design Variables',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.grid()
plt.legend()
plt.xlabel('Optimization Iteration')
plt.ylabel('Objective Function')

plt.figure(6,figsize=(20,16),dpi=120)
plt.plot(eval4,cl4,label='Coupled Design Variables',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.grid()
plt.legend()
plt.xlabel('Evaluations')
plt.ylabel('CL')

plt.figure(7,figsize=(20,16),dpi=120)
plt.plot(eval4,cd4,label='Coupled Design Variables',marker='x',linestyle='--',linewidth=3,markersize=20)
plt.grid()
plt.legend(loc='right')
plt.xlabel('Evaluations')
plt.ylabel('CD')

plt.show()
