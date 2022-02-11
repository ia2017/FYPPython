#!/usr/bin/python

# Importing python scripts
import os, sys
sys.path.insert(1, '/Users/imran/Documents/SU2/SU2Parallel/bin')
import finite_differences as fd
import continuous_adjoint as cadj
import discrete_adjoint as dadj
import direct_differentiation as ddiff
from csv import writer
import pandas as pd

# Function to get number of variables from FFD
def getvariablenumber(file):
    f = open(file,'r')
    # Finding line where CFL number is
    i = 0
    for line in f:
        if 'FFD_DEGREE' in line:
            c = i
        i=i+1

    f.seek(0)
    lines = f.readlines()
    #print(lines[c])
    i=0
    deg=1
    temp=''
    for char in lines[c]:
        if char.isdigit() == True:
            temp=temp+char
        elif temp!='' and char.isdigit() == False and temp!='0':
            deg=deg*(int(temp)+1)
            temp=''
        else:
            temp=''

    f.close()

    return deg

# ------- Input parameters ---------
file = 'config.cfg'
partition = 1
quiet = False
nzones = 2
step = 1e-4
compute = True
validate = False
mode = 'all'

# ----- Defining united file ------
f = open('of_grad_compare.csv', 'w', newline='')
csv_writer = writer(f)

# Defining header with design variables
header = []
header.append('DV')
n=getvariablenumber(file)
for i in range(0,n):
    header.append(i)
csv_writer.writerow(header)
f.close()

# ------ Executing gradient evaluation ---------

# --- Finite Difference ----
fd.finite_differences(file,partition,quiet,nzones)

os.chdir('FINDIFF')

# Putting into file
if os.path.exists('of_grad_findiff.csv'):
    findiff=pd.read_csv('of_grad_findiff.csv')
    header = findiff.head(0)
    i = 0
    for head in header:
        if "DRAG" in head:
            d = i
        i=i+1

    findiff=findiff.to_numpy()
    draggrad=findiff[:,d]

    # Writing to file
    os.chdir('..')
    f = open('of_grad_compare.csv', 'a', newline='')
    csv_writer = writer(f)
    draggrad=draggrad.tolist()
    FD=[]
    FD.append('FD')
    for num in draggrad:
        FD.append(num)
    csv_writer.writerow(FD)
    f.close()

# ---- Discrete Adjoint -----
dadj.discrete_adjoint(file,partition,step,nzones,mode)

# Putting into file
if os.path.exists('of_grad_cd.csv'):
    findiff=pd.read_csv('of_grad_cd.csv')
    header = findiff.head(0)
    i = 0
    for head in header:
        if "GRADIENT" in head:
            d = i
        i=i+1

    findiff=findiff.to_numpy()
    draggrad=findiff[:,d]

    # Writing to file
    f = open('of_grad_compare.csv', 'a', newline='')
    csv_writer = writer(f)
    draggrad=draggrad.tolist()
    FD=[]
    FD.append('Adjoint')
    for num in draggrad:
        FD.append(num)
    csv_writer.writerow(FD)
    f.close()


#cadj.continuous_adjoint(file,partition,compute,step,1)
#ddiff.direct_differentiation(file,partition,quiet,nzones)

