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

cp_init=pd.read_csv('multipointinit.csv')
cp_final=pd.read_csv('multipointfinal.csv')

x1=cp_init['Points_X'].to_numpy()
x1=x1-x1[0]
x11=cp_final['Points_X'].to_numpy()
x11=x11-x11[0]


cp1=cp_init['Pressure_Coefficient'].to_numpy()
cp11=cp_final['Pressure_Coefficient'].to_numpy()



plt.figure(figsize=(20,16))
plt.scatter(x1,-cp1,label='Initial')
plt.scatter(x11,-cp11,label='Optimised')
plt.grid()
plt.xlabel('x')
plt.ylabel('-Cp')
plt.legend()
plt.title('Cp Plot')

plt.show()