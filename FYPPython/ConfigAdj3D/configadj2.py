import pandas as pd
import time
import os
import subprocess

# ----- Listing options -----
linearsolver=['BCGSTAB', 'FGMRES', 'CONJUGATE_GRADIENT', 'SMOOTHER']
prec=['ILU', 'JACOBI', 'LU_SGS', 'LINELET']
convnum_central=['JST', 'LAX-FRIEDRICH']
convnum_upwind=['ROE','AUSM','MSW']
convnum_all=['JST', 'LAX-FRIEDRICH','ROE','AUSM']

# ----- For SU2_CFD -----
filename='configunswept.cfg'
nZone=2
nproc=4

# ----- Defining output files -----
f_iter = open('iter.csv','w',newline='')
f_ss=open('ss.csv','w',newline='')
f_resrho=open('resrho.csv','w',newline='')
f_resrhou=open('resrhou.csv','w',newline='')
f_resrhov=open('resrhov.csv','w',newline='')
f_resrhoE=open('resrhoE.csv','w',newline='')
f_time=open('time.dat','w')

f_iter.close()
f_ss.close()
f_resrho.close()
f_resrhou.close()
f_resrhov.close()
f_resrhoE.close()
f_time.close()

# ------ Opening configFLOW.cfg ------
config=open('configFLOW.cfg','r')
lines=config.readlines()

# Checking each line
i=0
for line in lines:
    if 'LINEAR_SOLVER=' in line:
        if 'DEFORM' in line:
            DLS=i
        else:
            LS=i
    if 'LINEAR_SOLVER_PREC=' in line:
        if 'DEFORM' in line:
            DLSP = i
        else:
            LSP = i
    if 'DISCADJ_LIN_SOLVER=' in line:
        DLS=i
    if 'DISCADJ_LIN_PREC=' in line:
        DLP=i
    if 'MGLEVEL=' in line:
        multigrid=i
    if 'CONV_NUM_METHOD_FLOW=' in line:
        CNMF=i
    if 'TIME_DISCRE_FLOW=' in line:
        timeflow=i
    if 'CONV_NUM_METHOD_ADJFLOW=' in line:
        CNMA=i
    if 'TIME_DISCRE_ADJFLOW=' in line:
        timeadj=i
    i+=1

config.close()

lines[CNMF] = 'CONV_NUM_METHOD_FLOW= ' + 'JST' + '\n'

# ------------------------------------
# -------- Running ADJOINT ---------
# ------------------------------------

# --------- Starting Iteration ---------

iter=0

# ------ Opening config.cfg to change to DISCRETE_ADJOINT ------

config2=open('configunswept.cfg','r')
lines2=config2.readlines()
i=0
for line in lines2:
    if 'MATH_PROBLEM=' in line:
        math=i
    i+=1
config2.close()

print(lines2[math])

lines2[math]='MATH_PROBLEM= DISCRETE_ADJOINT' + '\n'
config2=open('configunswept.cfg','w')
config2.writelines(lines2)
config2.close()

print(lines2[math])

for opt in convnum_all:

    # ------ Editing Adjoint Convective method -------
    lines[CNMA]='CONV_NUM_METHOD_ADJFLOW= ' + opt + '\n'
    lines[CNMF] = 'CONV_NUM_METHOD_FLOW= ' + opt + '\n'

    # ---- Editing file with new inputs -------
    config=open('configFLOW.cfg','w')
    config.writelines(lines)
    config.close()

    # ----- Starting SU2_CFD -------
    start = time.time()  # Starting clock

    p1 = subprocess.run(['mpiexec', '-n', str(nproc),'SU2_CFD_AD',filename])

    end = time.time()
    f_time=open('time.dat','a')
    f_time.write(opt + ' = ' + str(end-start) + 's' + '\n')

    # ------ Post Processing --------
    f_history = pd.read_csv('history_0.csv')
    f_adj= pd.read_csv('fsisteady_adj_res_cd_0.csv')
    f_history.columns=f_history.columns.str.replace('"','')

    ss=f_adj['Surface_Sensitivity']
    size_history=f_history.shape
    totaliter=pd.DataFrame({opt:range(0,size_history[0])})
    #print(f_history.columns)
    res_rho = f_history['   rms[A_Rho]   ']
    res_rhou = f_history['   rms[A_RhoU]  ']
    res_rhov = f_history['   rms[A_RhoV]  ']
    res_rhoE = f_history['    rms[A_E]    ']
    if iter==0:
        ss=pd.DataFrame({opt:ss})
        res_rho=pd.DataFrame({opt:res_rho})
        res_rhou = pd.DataFrame({opt: res_rhou})
        res_rhov = pd.DataFrame({opt: res_rhov})
        res_rhoE = pd.DataFrame({opt: res_rhoE})
        ss.to_csv('ss.csv',index=False)
        totaliter.to_csv('iter.csv',index=False)
        res_rho.to_csv('resrho.csv',index=False)
        res_rhou.to_csv('resrhou.csv',index=False)
        res_rhov.to_csv('resrhov.csv',index=False)
        res_rhoE.to_csv('resrhoE.csv',index=False)
    else:
        ss = pd.DataFrame({opt: ss})
        res_rho = pd.DataFrame({opt: res_rho})
        res_rhou = pd.DataFrame({opt: res_rhou})
        res_rhov = pd.DataFrame({opt: res_rhov})
        res_rhoE = pd.DataFrame({opt: res_rhoE})
        f_ss = pd.read_csv('ss.csv')
        f_ss=pd.concat([f_ss,ss], axis=1)
        f_ss.to_csv('ss.csv',index=False)
        f_iter=pd.read_csv('iter.csv')
        f_iter=pd.concat([f_iter,totaliter], axis=1)
        f_iter.to_csv('iter.csv',index=False)
        f_resrho=pd.read_csv('resrho.csv')
        f_resrho=pd.concat([f_resrho,res_rho], axis=1)
        f_resrho.to_csv('resrho.csv',index=False)
        f_resrhou = pd.read_csv('resrhou.csv')
        f_resrhou=pd.concat([f_resrhou,res_rhou], axis=1)
        f_resrhou.to_csv('resrhou.csv', index=False)
        f_resrhov = pd.read_csv('resrhov.csv')
        f_resrhov=pd.concat([f_resrhov,res_rhov], axis=1)
        f_resrhov.to_csv('resrhov.csv', index=False)
        f_resrhoE = pd.read_csv('resrhoE.csv')
        f_resrhoE=pd.concat([f_resrhoE,res_rhoE], axis=1)
        f_resrhoE.to_csv('resrhoE.csv', index=False)

    iter+=1


