import pysu2
import pysu2ad
import os

# ----- For SU2_CFD -----
filename='config.cfg'
nZone=2
from mpi4py import MPI
comm=MPI.COMM_WORLD

SU2Driver = pysu2.CMultizoneDriver(filename, nZone, comm);
SU2Driver.StartSolver()

# ----- Starting SU2_CFD -------
# Renaming files
os.rename('fsisteady_res_0.csv','fsisteady_0.csv')
os.rename('fsisteady_res_0.dat','fsisteady_0.dat')
os.rename('fsisteady_res_1.csv','fsisteady_1.csv')
os.rename('fsisteady_res_1.dat','fsisteady_1.dat')

SU2Driver = pysu2ad.CDiscAdjSinglezoneDriver(filename, nZone, comm);
SU2Driver.StartSolver()







