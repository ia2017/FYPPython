import matplotlib.pyplot as plt
import pandas as pd

SIZEPLT = 28
plt.rc('font', size=SIZEPLT)          # controls default text sizes
plt.rc('axes', titlesize=SIZEPLT)     # fontsize of the axes title
plt.rc('axes', labelsize=SIZEPLT)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('legend', fontsize=SIZEPLT)    # legend fontsize
plt.rc('figure', titlesize=SIZEPLT)  # fontsize of the figure title

cp1=pd.read_csv('Cpplot.csv')
cp2=pd.read_csv('CpPlot2.csv')
x1=cp1['Points_X'].to_numpy()
x1=x1-x1[0]
cp11=cp1['Pressure_Coefficient'].to_numpy()
x2=cp2['Points_X'].to_numpy()
x2=x2-x2[0]
cp21=cp2['Pressure_Coefficient'].to_numpy()



plt.figure(figsize=(20,16))
plt.scatter(x1,-cp11,label='Initial Sweep')
plt.scatter(x2,-cp21,label='Final Sweep')
plt.grid()
plt.xlabel('$x$ (m)')
plt.ylabel('-$C_p$')
plt.legend()
plt.title('$C_p$ Plot')


plt.show()