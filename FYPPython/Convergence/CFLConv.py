from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
SIZEPLT = 15
plt.rc('font', size=SIZEPLT)          # controls default text sizes
plt.rc('axes', titlesize=SIZEPLT)     # fontsize of the axes title
plt.rc('axes', labelsize=SIZEPLT)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('legend', fontsize=SIZEPLT)    # legend fontsize
plt.rc('figure', titlesize=SIZEPLT)  # fontsize of the figure title

# FLOW
# data extraction
data=pd.read_csv('CFL4.csv')
size=data.shape
data=data.to_numpy()

# Sorting
cfl=data[:,0]
iter=data[:,1]
CL=data[:,2]
CD=data[:,3]

# ----- Plots -------
plt.figure(1,figsize=(10, 8), dpi=200)
plt.title('Total Iter vs CFL')
#plt.plot(cfl,iter,linestyle='-', marker='.',markersize='2',linewidth='2')
plt.plot(cfl,iter)
plt.ylabel('Total iter')
plt.xlabel('CFL no.')
plt.ylim(0,10000)
plt.xlim(0,1000)
plt.grid()

plt.figure(2,figsize=(10, 8), dpi=200)
plt.title('Force Coefficients vs CFL')
plt.plot(cfl,CL,label='CL')
plt.plot(cfl,CD,label='CD')
plt.xlabel('CFL no.')
plt.legend()
plt.xlim(0,1000)
plt.ylim(0,0.5)
plt.grid()



plt.show()


