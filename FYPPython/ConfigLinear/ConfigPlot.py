import matplotlib.pyplot as plt
import pandas as pd

cl=pd.read_csv('cl.csv')
cd=pd.read_csv('cd.csv')
resrho=pd.read_csv('resrho.csv')
resrhou=pd.read_csv('resrhou.csv')
resrhov=pd.read_csv('resrhov.csv')
resrhoE=pd.read_csv('resrhoE.csv')

cl.plot()
plt.show()