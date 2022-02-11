import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Reading data

matched=pd.read_csv('Displacement.csv')
nn=pd.read_csv('Displacement_nn.csv')
rbf_tps=pd.read_csv('Displacement_rbftps_unmatched2.csv')
rbf_tps_2=pd.read_csv('Displacement_rbftps_unmatched2_2.csv')
rbf_tps_0_5=pd.read_csv('Displacement_rbftps_unmatched2_0_5.csv')
rbf_tps_5=pd.read_csv('Displacement_rbftps_unmatched2_5.csv')
rbf_wend=pd.read_csv('Displacement_rbfwend_unmatched2.csv')
rbf_wend_2=pd.read_csv('Displacement_rbfwend_unmatched2_2.csv')
rbf_wend_0_5=pd.read_csv('Displacement_rbfwend_unmatched2_0_5.csv')
rbf_wend_5=pd.read_csv('Displacement_rbfwend_unmatched2_5.csv')

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
disp_rbf_tps_5=rbf_tps_5['Displacement_Magnitude']
stress_rbf_tps_5=rbf_tps_5['Von_Mises_Stress']
disp_rbf_wend_5=rbf_wend_5['Displacement_Magnitude']
stress_rbf_wend_5=rbf_wend_5['Von_Mises_Stress']



nn_diff=disp_nn-disp
nn_diff=nn_diff.to_numpy()
print(disp)
print(disp_nn)
print(np.amax(nn_diff))
norm_nn=np.linalg.norm(nn_diff)
print("norm_nn: "+str(norm_nn))


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
plt.plot(disp,linewidth=2,linestyle='-.',label='Matched')
plt.plot(disp_nn,linewidth=2,linestyle='-',marker='x',markersize='6',label='NN')
#plt.plot(disp_rbf_tps_0_5,linewidth=2,linestyle='-',marker='x',markersize='6',label='RBF TPS, r=0.05')
plt.plot(disp_rbf_tps,linewidth=2,linestyle='-',marker='o',markersize='6',label='RBF TPS, r=0.1')
plt.plot(disp_rbf_tps_2,linewidth=2,linestyle='-',marker='o',markersize='6',label='RBF TPS, r=0.2')
plt.plot(disp_rbf_tps_5,linewidth=2,linestyle='-',marker='o',markersize='6',label='RBF TPS, r=0.5')
#plt.plot(disp_rbf_wend_0_5,linewidth=2,linestyle='-',marker='x',markersize='6',label='RBF Wend C2, r=0.05')
plt.plot(disp_rbf_wend,linewidth=2,linestyle='-',marker='',markersize='6',label='RBF Wend C2, r=0.1')
#plt.plot(disp_rbf_wend_2,linewidth=2,linestyle='-',marker='',markersize='6',label='RBF Wend C2, r=0.2')
#plt.plot(disp_rbf_wend_5,linewidth=2,linestyle='-',marker='',markersize='6',label='RBF Wend C2, r=0.5')
plt.grid()
plt.ylabel('Displacement (m)')
plt.xlabel('Span (m)')
plt.legend()


plt.figure(2,figsize=(20,16),dpi=120)

plt.plot(stress,linewidth=2,linestyle='-.',label='Matched')
plt.plot(stress_nn,linewidth=2,linestyle='-',marker='o',markersize='6',label='NN')
plt.plot(stress_rbf_tps_0_5,linewidth=2,linestyle='-',marker='x',markersize='6',label='RBF TPS, r=0.05')
plt.plot(stress_rbf_tps,linewidth=2,linestyle='-',marker='x',markersize='6',label='RBF TPS, r=0.1')
plt.plot(stress_rbf_tps_2,linewidth=2,linestyle='-',marker='x',markersize='6',label='RBF TPS, r=0.2')
plt.plot(stress_rbf_tps_5,linewidth=2,linestyle='-',marker='x',markersize='6',label='RBF TPS, r=0.5')
plt.plot(stress_rbf_wend_0_5,linewidth=2,linestyle='-',marker='x',markersize='6',label='RBF Wend C2, r=0.05')
plt.plot(stress_rbf_wend,linewidth=2,linestyle='-',marker='x',markersize='6',label='RBF Wend C2, r=0.1')
plt.plot(stress_rbf_wend_2,linewidth=2,linestyle='-',marker='x',markersize='6',label='RBF Wend C2, r=0.2')
plt.plot(stress_rbf_wend_5,linewidth=2,linestyle='-',marker='x',markersize='6',label='RBF Wend C2, r=0.5')
plt.grid()
plt.ylabel('Von Mises Stress (Nm-2)')
plt.xlabel('Span (m)')
plt.legend()
plt.show()