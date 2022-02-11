import matplotlib.pyplot as plt
import pandas as pd

SIZEPLT = 28
plt.rc('font', size=SIZEPLT)          # controls default text sizes
plt.rc('axes', titlesize=SIZEPLT)     # fontsize of the axes title
plt.rc('axes', labelsize=SIZEPLT)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('legend', fontsize=SIZEPLT)    # legend fontsize
plt.rc('figure', titlesize=SIZEPLT)  # fontsize of the figure title

cl=pd.read_csv('cl.csv')
cd=pd.read_csv('cd.csv')
mesh=pd.read_csv('mesh.csv')

cl=cl.to_numpy()

plt.figure(1,figsize=[15,12],dpi=120)
plt.plot(mesh,cl,linestyle='-',marker='x',linewidth=3,markersize=7,label='CL')
plt.title('CL Mesh Convergence')
plt.xlabel('Mesh size')
plt.ylabel('CL')
plt.ylim(0.35,0.38)
plt.grid()

plt.figure(2,figsize=[15,12],dpi=120)
plt.plot(mesh,cd,linestyle='-',marker='x',linewidth=3,markersize=7,label='CD')
plt.title('CD Mesh Convergence')
plt.ylabel('CD')
plt.xlabel('Mesh size')
plt.ylim(0.01,0.03)
plt.grid()

plt.show()