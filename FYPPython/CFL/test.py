import os, shutil
import pandas as pd
from csv import writer

f=open('CFL.csv','w',newline='')
# Post Processing
data_flow = pd.read_csv('history_0.csv')
header=data_flow.head(0)
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
CFL=5
CL=data_flow[total_iter-1,l]
CD=data_flow[total_iter-1,d]

csv_writer=writer(f)
header=["CFL", "Total_Iter", "CL", "CD"]
csv_writer.writerow(header)
line_out=[CFL, total_iter,CL,CD]
csv_writer.writerow(line_out)
f.close()

f=open('CFL.csv','r')

lines=f.readlines()

print(lines)
f.close()
