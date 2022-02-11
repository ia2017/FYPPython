import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Reading data

matched=pd.read_csv('Displacement.csv')
nn=pd.read_csv('Displacment_unmatched3.csv')
rbf_tps=pd.read_csv('Displacement_rbftps_unmatched3.csv')
rbf_tps_2=pd.read_csv('Displacement_rbftps_unmatched3_2.csv')
rbf_tps_0_5=pd.read_csv('Displacement_rbftps_unmatched3_0_5.csv')
rbf_wend=pd.read_csv('Displacement_rbfwend_unmatched3.csv')
rbf_wend_2=pd.read_csv('Displacement_rbfwend_unmatched3_2.csv')
rbf_wend_0_5=pd.read_csv('Displacement_rbfwend_unmatched3_0_5.csv')
#refined=pd.read_csv('Displacement_refined.csv')
#unrefined=pd.read_csv('')
nn_unrefined=pd.read_csv('Displacement_unmatched2.csv')
rbf_tps_unrefined=pd.read_csv('Displacement_rbftps_unmatched2.csv')
rbf_wend_unrefined=pd.read_csv('Displacement_rbfwend_unmatched2.csv')


disp=matched['Displacement_Magnitude']
stress=matched['Von_Mises_Stress']
disp_nn=nn['Displacement_Magnitude']
stress_nn=nn['Von_Mises_Stress']
disp_rbf_tps=rbf_tps['Displacement_Magnitude']
stress_rbf_tps=rbf_tps['Von_Mises_Stress']
disp_rbf_wend=rbf_wend['Displacement_Magnitude']
stress_rbf_wend=rbf_wend['Von_Mises_Stress']
disp_rbf_tps_2=rbf_tps_2['Displacement_Magnitude']
stress_rbf_tps_2=rbf_tps_2['Von_Mises_Stress']
disp_rbf_wend_2=rbf_wend_2['Displacement_Magnitude']
stress_rbf_wend_2=rbf_wend_2['Von_Mises_Stress']
disp_rbf_tps_0_5=rbf_tps_0_5['Displacement_Magnitude']
stress_rbf_tps_0_5=rbf_tps_0_5['Von_Mises_Stress']
disp_rbf_wend_0_5=rbf_wend_0_5['Displacement_Magnitude']
stress_rbf_wend_0_5=rbf_wend_0_5['Von_Mises_Stress']
#disp_refined=refined['Displacement_Magnitude']
#stress_refined=refined['Von_Mises_Stress']
#disp_unrefined=unrefined['Displacement_Magnitude']
#stress_unrefined=unrefined['Von_Mises_Stress']
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
#plt.plot(disp_unrefined,linewidth=2,linestyle='-.',label='Unrefined Matched')
plt.plot(disp,linewidth=2,linestyle='-.',label='Moderate refined Matched')
#plt.plot(disp_refined,linewidth=2,linestyle='-.',label='Refined Matched')
plt.plot(disp_nn_unrefined,linewidth=2,linestyle='--',label='Unrefined NN')
plt.plot(disp_rbf_tps_unrefined,linewidth=2,linestyle='--',label='Unrefined RBF TPS')
plt.plot(disp_rbf_wend_unrefined,linewidth=2,linestyle='--',label='Unrefined RBF Wend C2')
plt.plot(disp_nn,linewidth=2,linestyle='-',marker='o',markersize='6',label='Moderate Refined NN')
plt.plot(disp_rbf_tps_0_5,linewidth=2,linestyle='-',marker='x',markersize='6',label='Moderate Refined RBF TPS, r=0.05')
plt.plot(disp_rbf_tps,linewidth=2,linestyle='-',marker='x',markersize='6',label='Moderate Refined RBF TPS, r=0.1')
plt.plot(disp_rbf_tps_2,linewidth=2,linestyle='-',marker='x',markersize='6',label='Moderate Refined RBF TPS, r=0.2')
plt.plot(disp_rbf_wend_0_5,linewidth=2,linestyle='-',marker='x',markersize='6',label='Moderate Refined RBF Wend C2, r=0.05')
plt.plot(disp_rbf_wend,linewidth=2,linestyle='-',marker='x',markersize='6',label='Moderate Refined RBF Wend C2, r=0.1')
plt.plot(disp_rbf_wend_2,linewidth=2,linestyle='-',marker='x',markersize='6',label='Moderate Refined RBF Wend C2, r=0.2')
plt.grid()
plt.ylabel('Displacement (m)')
plt.xlabel('Span (m)')
plt.legend()


plt.figure(2,figsize=(20,16),dpi=120)
#plt.plot(stress_unrefined,linewidth=2,linestyle='-.',label='Unrefined Matched')
plt.plot(stress,linewidth=2,linestyle='-.',label='Moderate Refined Matched')
#plt.plot(stress_refined,linewidth=2,linestyle='-.',label='Refined Matched')
plt.plot(stress_nn_unrefined,linewidth=2,linestyle='--',label='Unrefined NN')
plt.plot(stress_rbf_tps_unrefined,linewidth=2,linestyle='--',label='Unrefined RBF TPS')
plt.plot(stress_rbf_wend_unrefined,linewidth=2,linestyle='--',label='Unrefined RBF Wend C2')
plt.plot(stress_nn,linewidth=2,linestyle='-',marker='o',markersize='6',label='Moderate Refined NN')
plt.plot(stress_rbf_tps_0_5,linewidth=2,linestyle='-',marker='x',markersize='6',label='Moderate Refined RBF TPS, r=0.05')
plt.plot(stress_rbf_tps,linewidth=2,linestyle='-',marker='x',markersize='6',label='Moderate Refined RBF TPS, r=0.1')
plt.plot(stress_rbf_tps_2,linewidth=2,linestyle='-',marker='x',markersize='6',label='Moderate Refined RBF TPS, r=0.2')
plt.plot(stress_rbf_wend_0_5,linewidth=2,linestyle='-',marker='x',markersize='6',label='Moderate Refined RBF Wend C2, r=0.05')
plt.plot(stress_rbf_wend,linewidth=2,linestyle='-',marker='x',markersize='6',label='Moderate Refined RBF Wend C2, r=0.1')
plt.plot(stress_rbf_wend_2,linewidth=2,linestyle='-',marker='x',markersize='6',label='Moderate Refined RBF Wend C2, r=0.2')
plt.grid()
plt.ylabel('Von Mises Stress (Nm-2)')
plt.xlabel('Span (m)')
plt.legend()
plt.show()