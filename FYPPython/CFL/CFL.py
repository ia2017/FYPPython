#!/usr/bin/python
import pysu2
import pandas as pd
from csv import writer

# ----- Input -----
n=10

# -------- Defining csv file ---------
f=open('CFL.csv','w',newline='')
csv_writer=writer(f)
header=["CFL", "Total_Iter", "CL", "CD"]
csv_writer.writerow(header)
f.close()

# --------- Iterating for each CFL number ---------

for int in range(1,n):

    # Defining current cfl number
    cfl=int/2

    # Reading config.cfg file
    config=open('configFLOW.cfg','r')

    # Finding line where CFL number is
    i=0
    for line in config:
        if 'CFL_NUMBER' in line:
            c=i
        i=i+1

    config.seek(0)
    lines=config.readlines()
    print(lines[c])
    config.close()

    # Editing config file to new CFL number

    lines[c]='CFL_NUMBER= ' + str(cfl) + '\n'
    config=open('configFLOW.cfg','w')
    config.writelines(lines)
    config.close()

    # Starting SU2_CFD
    filename='config.cfg'
    nZone=2
    from mpi4py import MPI
    comm=MPI.COMM_WORLD

    SU2Driver = pysu2.CMultizoneDriver(filename, nZone, comm);
    SU2Driver.StartSolver()

    # ------ Post Processing --------

    f = open('CFL.csv','a',newline='')
    csv_writer = writer(f)
    data_flow = pd.read_csv('history_0.csv')

    # Finding CL and CD in history file header
    header = data_flow.head(0)
    i=0
    for head in header:
        if "CL" in head:
            l=i
        if "CD" in head:
            d=i
        i+=1

    data_flow=data_flow.to_numpy()
    size = data_flow.shape
    total_iter=size[0]
    CL=data_flow[total_iter-1,l]
    CD=data_flow[total_iter-1,d]

    # Transferring data to csv file
    line_out = [cfl, total_iter, CL, CD]
    csv_writer.writerow(line_out)

    f.close()   # Closing file
