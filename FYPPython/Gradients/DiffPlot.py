from matplotlib import pyplot as plt
import numpy as np

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