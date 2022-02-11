import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Reading data

matched=pd.read_csv('Displacement.csv')
nn=pd.read_csv('Displacement_nn.csv')
rbf_tps=pd.read_csv('Displacement_rbf_tps.csv')
rbf_wend=pd.read_csv('Displacement_rbf_wend.csv')
refined=pd.read_csv('Displacement_refined.csv')
unrefined=pd.read_csv('Displacement_old.csv')
nn_unrefined=pd.read_csv('Displacement_nn_old.csv')
rbf_tps_unrefined=pd.read_csv('Displacement_rbf_tps_old.csv')
rbf_wend_unrefined=pd.read_csv('Displacement_rbf_wend_old.csv')


disp=matched['Displacement_Magnitude']
stress=matched['Von_Mises_Stress']
disp_nn=nn['Displacement_Magnitude']
stress_nn=nn['Von_Mises_Stress']
disp_rbf_tps=rbf_tps['Displacement_Magnitude']
stress_rbf_tps=rbf_tps['Von_Mises_Stress']
disp_rbf_wend=rbf_wend['Displacement_Magnitude']
stress_rbf_wend=rbf_wend['Von_Mises_Stress']
disp_refined=refined['Displacement_Magnitude']
stress_refined=refined['Von_Mises_Stress']
disp_unrefined=unrefined['Displacement_Magnitude']
stress_unrefined=unrefined['Von_Mises_Stress']
disp_nn_unrefined=nn_unrefined['Displacement_Magnitude']
stress_nn_unrefined=nn_unrefined['Von_Mises_Stress']
disp_rbf_tps_unrefined=rbf_tps_unrefined['Displacement_Magnitude']
stress_rbf_tps_unrefined=rbf_tps_unrefined['Von_Mises_Stress']
disp_rbf_wend_unrefined=rbf_wend_unrefined['Displacement_Magnitude']
stress_rbf_wend_unrefined=rbf_wend_unrefined['Von_Mises_Stress']

rbf_diff=disp_rbf_tps-disp_rbf_wend
rbf_diff=rbf_diff.to_numpy()
norm_rbf=np.linalg.norm(rbf_diff)
print(norm_rbf)


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
plt.plot(disp_unrefined,linewidth=2,linestyle='-.',label='Unrefined Matched')
plt.plot(disp,linewidth=2,linestyle='-.',label='Moderate refined Matched')
plt.plot(disp_refined,linewidth=2,linestyle='-.',label='Refined Matched')
plt.plot(disp_nn_unrefined,linewidth=2,linestyle='--',label='Unrefined NN')
plt.plot(disp_rbf_tps_unrefined,linewidth=2,label='Unrefined RBF TPS')
plt.plot(disp_rbf_wend_unrefined,linewidth=2,linestyle='--',label='Unrefined RBF Wend C2')
plt.plot(disp_nn,linewidth=2,linestyle='--',label='Moderate Refined NN')
plt.plot(disp_rbf_tps,linewidth=2,label='Moderate Refined RBF TPS')
plt.plot(disp_rbf_wend,linewidth=2,linestyle='--',label='Moderate Refined RBF Wend C2')
plt.grid()
plt.ylabel('Displacement (m)')
plt.xlabel('Span (m)')
plt.legend()


plt.figure(2,figsize=(20,16),dpi=120)
plt.plot(stress_unrefined,linewidth=2,linestyle='-.',label='Unrefined Matched')
plt.plot(stress,linewidth=2,linestyle='-.',label='Moderate Refined Matched')
plt.plot(stress_refined,linewidth=2,linestyle='-.',label='Refined Matched')
plt.plot(stress_nn_unrefined,linewidth=2,linestyle='-.',label='Unrefined NN')
plt.plot(stress_rbf_tps_unrefined,linewidth=2,label='Unrefined RBF TPS')
plt.plot(stress_rbf_wend_unrefined,linewidth=2,linestyle='--',label='Unrefined RBF Wend C2')
plt.plot(stress_nn,linewidth=2,label='Moderate Refined NN')
plt.plot(stress_rbf_tps,linewidth=2,linestyle='--',label='Moderate Refined RBF TPS')
plt.plot(stress_rbf_wend,linewidth=2,linestyle='--',label='Moderate Refined RBF Wend C2')
plt.grid()
plt.ylabel('Von Mises Stress (Nm-2)')
plt.xlabel('Span (m)')
plt.legend()
plt.show()