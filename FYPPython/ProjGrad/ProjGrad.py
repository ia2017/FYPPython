from matplotlib import pyplot as plt
import numpy as np

f=open('of_grad_new3.dat','r')
next(f)
new3=f.read().splitlines()
chars=''
f.close()

f=open('of_grad_new6.dat','r')
next(f)
new6=f.read().splitlines()
chars=''
f.close()

f=open('of_grad_new3deform.dat','r')
next(f)
new6def=f.read().splitlines()
chars=''
f.close()

#f=open('of_grad_new7.dat','r')
#next(f)
#new7=f.read().splitlines()
#chars=''
#f.close()

grad_new3=[]
grad_new6=[]
grad_new6def=[]
#grad_new7=[]

for line in new3:
    grad_new3.append(-float(line))

for line in new6:
    grad_new6.append(-float(line))

for line in new6def:
    grad_new6def.append(-float(line))

#for line in new7:
#    grad_new7.append(-float(line))

y=np.arange(1.8,2.1,0.03)


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
plt.plot(y,grad_new3,label='Original (undeformed)',marker='x',linestyle='-',linewidth=3,markersize=15)
plt.plot(y,grad_new6def,label='Original (pre-deformed)',marker='x',linestyle='-',linewidth=3,markersize=15)
plt.plot(y,grad_new6,label='Symmetric tip',marker='x',linestyle='-',linewidth=3,markersize=15)
#plt.plot(y,grad_new7,label='Symmetric tip, Lower AR',marker='x',linestyle='-',linewidth=3,markersize=15)
plt.grid()
plt.legend()
plt.xlabel('Spanwise coordinate')
plt.ylabel('$C_D$ Gradient')
plt.show()