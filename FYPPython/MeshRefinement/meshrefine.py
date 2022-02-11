import subprocess
import pysu2
import os
import pandas as pd

f_cl=open('cl.csv','w',newline='')
f_cd=open('cd.csv','w',newline='')
f_mesh=open('mesh.csv','w',newline='')
f_cl.close()
f_cd.close()
f_mesh.close()

filename='config.cfg'
nZone=1
from mpi4py import MPI
comm=MPI.COMM_WORLD

# Changing lc
#lc=0.1
#dlc=0.01
#total=lc/dlc
#lc=lc+dlc

# Changing le
le=0.02
dle=0.002
total=le/dle
le=le+dle
# ----- Start loop -------

for iter in range(0,int(total)-1):

    #Changing lc
    #lc=lc-dlc
    #le=0.01

    #Changing le
    lc = 0.05
    le = le - dle

    # ------ Opening flow geo ------
    flow=open('NACA2412_3D_flow.geo','r')
    lines=flow.readlines()

    # Checking each line
    i=0
    for line in lines:
        if 'lc=' in line:
            nlc = i
        if 'le=' in line:
            nle = i
        i+=1
    flow.close()

    # ------ Editing New points -------
    lines[nlc]='lc=' + str(lc) + ';\n'
    lines[nle]='le=' + str(le) + ';\n'

    # ---- Editing file with new inputs -------
    flow=open('NACA2412_3D_flow.geo','w')
    flow.writelines(lines)
    flow.close()

    p1=subprocess.run(['gmsh','NACA2412_3D_flow.geo','-3', '-o', 'NACA2412_3D_flow', '-format', 'su2'])
    os.rename('NACA2412_3D_flow','NACA2412_3D_flow.su2')

    SU2Driver = pysu2.CSinglezoneDriver(filename, nZone,comm);
    SU2Driver.StartSolver()

    f_history = pd.read_csv('history.csv')
    f_history.columns=f_history.columns.str.replace('"','')
    cl=f_history['       CL       ']
    cd=f_history['       CD       ']

    cl1=cl.tail(1)
    cd1=cd.tail(1)
    cl1=cl1.to_numpy()
    cd1=cd1.to_numpy()

    if iter==0:
        cl2=pd.DataFrame({'CL':cl1})
        cd2=pd.DataFrame({'CD':cd1})
        mesh2=pd.DataFrame({'lc':le},index=[i])
        cl2.to_csv('cl.csv',index=False)
        cd2.to_csv('cd.csv',index=False)
        mesh2.to_csv('mesh.csv',index=False)
    else:
        cl2 = pd.DataFrame({'CL': cl1})
        f_cl = pd.read_csv('cl.csv')
        f_cl = pd.concat([f_cl, cl2])
        f_cl.to_csv('cl.csv', index=False)
        cd2 = pd.DataFrame({'CD': cd1})
        f_cd = pd.read_csv('cd.csv')
        f_cd = pd.concat([f_cd, cd2])
        f_cd.to_csv('cd.csv', index=False)
        mesh2 = pd.DataFrame({'lc':le},index=[i])
        f_mesh = pd.read_csv('mesh.csv')
        f_mesh = pd.concat([f_mesh, mesh2])
        f_mesh.to_csv('mesh.csv', index=False)