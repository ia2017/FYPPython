import pysu2

# ----- For SU2_CFD -----
filename='config.cfg'
nZone=2
from mpi4py import MPI
comm=MPI.COMM_WORLD

# ---- Initiate SU2_CFD -----
SU2Driver = pysu2.CSinglezoneDriver(filename, nZone, comm);
SU2Driver.StartSolver()