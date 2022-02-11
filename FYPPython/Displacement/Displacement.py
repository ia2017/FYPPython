import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Reading data

matched=pd.read_csv('Displacementwinglet0orig.csv')
nn=pd.read_csv('Displacementwingletorig.csv')
rbf_tps=pd.read_csv('displacementwingletfinal.csv')


disp=matched['Displacement_Magnitude']
stress=matched['Von_Mises_Stress']
disp_nn=nn['Displacement_Magnitude']
stress_nn=nn['Von_Mises_Stress']
disp_rbf_tps=rbf_tps['Displacement_Magnitude']
stress_rbf_tps=rbf_tps['Von_Mises_Stress']





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
plt.plot(disp,linewidth=2,linestyle='-.',label='Original (undeformed)')
plt.plot(disp_nn,linewidth=2,linestyle='-.',marker='',markersize='6',label='Original (pre-deformed)')
plt.plot(disp_rbf_tps,linewidth=2,linestyle='-',marker='',markersize='6',label='Optimised')

plt.grid()
plt.ylabel('Displacement (m)')
plt.xlabel('Span (m)')
plt.legend()


plt.figure(2,figsize=(20,16),dpi=120)

plt.plot(stress,linewidth=2,linestyle='-.',label='Original (undeformed)')
plt.plot(stress_nn,linewidth=2,linestyle='-.',marker='',markersize='6',label='Original (pre-deformed)')
plt.plot(stress_rbf_tps,linewidth=2,linestyle='-',marker='',markersize='6',label='Optimised')
plt.grid()
plt.ylabel('Von Mises Stress (Nm-2)')
plt.xlabel('Span (m)')
plt.legend()
plt.show()