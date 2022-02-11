from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# FLOW
# data extraction
data_flow=pd.read_csv('history_0.csv')
size=data_flow.shape
data_flow=data_flow.to_numpy()
total_iter=np.linspace(0,size[0]-1,size[0])

# data sorting
outer_iter=data_flow[:,1]
inner_iter=data_flow[:,2]
rms_rho=data_flow[:,3]
rms_rhou=data_flow[:,4]
rms_rhov=data_flow[:,5]
rms_rhow=data_flow[:,6]
rms_rhoE=data_flow[:,7]
CD=data_flow[:,8]
CL=data_flow[:,9]

# FEA
# data extraction
data_fea=pd.read_csv('history_1.csv')
size_fea=data_fea.shape
data_fea=data_fea.to_numpy()
total_iter_fea=np.linspace(0,size_fea[0]-1,size_fea[0])

# data sorting
outer_iter_fea=data_fea[:,1]
inner_iter_fea=data_fea[:,2]
rms_u_fea=data_fea[:,3]
rms_R_fea=data_fea[:,4]
rms_E_fea=data_fea[:,5]
rms_dispx=data_fea[:,6]
rms_dispy=data_fea[:,7]
rms_dispz=data_fea[:,8]

# -------- Plots ----------

plt.figure(1)
plt.title('Flow Residuals')
plt.plot(total_iter,rms_rho,label='rms_rho')
plt.plot(total_iter,rms_rhou,label='rms_rhou')
plt.plot(total_iter,rms_rhov,label='rms_rhov')
plt.plot(total_iter,rms_rhow,label='rms_rhow')
plt.plot(total_iter,rms_rhoE,label='rms_rhoE')
plt.xlabel('Total Iter')
plt.legend()
plt.grid()

plt.figure(2)
plt.title('Force Coefficients')
plt.plot(total_iter,CL,label='CL')
plt.plot(total_iter,CD,label='CD')
plt.xlabel('Total Iter')
plt.legend()
plt.grid()

plt.figure(3)
plt.title('FEA Residuals')
plt.plot(total_iter_fea,rms_u_fea,label='rms_rho')
plt.plot(total_iter_fea,rms_R_fea,label='rms_rhou')
plt.plot(total_iter_fea,rms_E_fea,label='rms_rhov')
plt.xlabel('Total Iter')
plt.legend()
plt.grid()

plt.figure(4)
plt.title('rms Disp')
plt.plot(total_iter_fea,rms_dispx,label='rms_dispx')
plt.plot(total_iter_fea,rms_dispy,label='rms_dispy')
plt.plot(total_iter_fea,rms_dispz,label='rms_dispz')
plt.xlabel('Total Iter')
plt.legend()
plt.grid()

plt.show()