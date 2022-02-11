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
resrho=pd.read_csv('resrho.csv')
resrhou=pd.read_csv('resrhou.csv')
resrhov=pd.read_csv('resrhov.csv')
resrhoE=pd.read_csv('resrhoE.csv')


cd.plot(figsize=(20,16),linewidth=3)
plt.grid()
plt.xlabel('Total Iterations')
plt.ylabel('Cd')
plt.title('Cd convergence')
resrhou.plot(figsize=(20,16),linewidth=3)
plt.title('Residuals')
plt.xlabel('Total Iterations')
plt.ylabel('log(Residuals)')
plt.grid()
plt.show()