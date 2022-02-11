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

cp2_new3=pd.read_csv('cp2_new3.csv')
cp208_new3=pd.read_csv('cp2.08_new3.csv')
cp19_new3def=pd.read_csv('cp1.9_new3def.csv')
cp204_new3def=pd.read_csv('cp2.04_new3def.csv')

cp2_new6=pd.read_csv('cp2_new6.csv')
cp208_new6=pd.read_csv('cp2.09_new6.csv')
cp2_new6def=pd.read_csv('cp2_new6def.csv')
cp208_new6def=pd.read_csv('cp2.08_new6def.csv')
cp19_new6defup=pd.read_csv('cp1.9_new6defup.csv')
cp203_new6defup=pd.read_csv('cp2.03_new6defup.csv')

x1=cp2_new3['Points_X'].to_numpy()
x1=x1-x1[0]
x11=cp19_new3def['Points_X'].to_numpy()
x11=x11-x11[0]
x2=cp208_new3['Points_X'].to_numpy()
x2=x2-x2[0]
x21=cp204_new3def['Points_X'].to_numpy()
x21=x21-x21[0]
x3=cp2_new6['Points_X'].to_numpy()
x3=x3-x3[0]
x31=cp2_new6def['Points_X'].to_numpy()
x31=x31-x31[0]
x4=cp208_new6['Points_X'].to_numpy()
x4=x4-x4[0]
x41=cp208_new6def['Points_X'].to_numpy()
x41=x41-x41[0]
x32=cp19_new6defup['Points_X'].to_numpy()
x32=x32-x32[0]+0.04
x42=cp203_new6defup['Points_X'].to_numpy()
x42=x42-x42[0]+0.05

cp1=cp2_new3['Pressure_Coefficient'].to_numpy()
cp2=cp208_new3['Pressure_Coefficient'].to_numpy()
cp11=cp19_new3def['Pressure_Coefficient'].to_numpy()
cp21=cp204_new3def['Pressure_Coefficient'].to_numpy()
cp3=cp2_new6['Pressure_Coefficient'].to_numpy()
cp4=cp208_new6['Pressure_Coefficient'].to_numpy()
cp31=cp2_new6def['Pressure_Coefficient'].to_numpy()
cp41=cp208_new6def['Pressure_Coefficient'].to_numpy()
cp32=cp19_new6defup['Pressure_Coefficient'].to_numpy()
cp42=cp203_new6defup['Pressure_Coefficient'].to_numpy()


plt.figure(figsize=(20,16))
plt.scatter(x1,-cp1,label='Initial')
plt.scatter(x11,-cp11,label='Deformed')
plt.grid()
plt.xlabel('x')
plt.ylabel('Cp')
plt.legend()
plt.title('Cp Plot')

plt.figure(figsize=(20,16))
plt.scatter(x2,-cp2,label='Initial')
plt.scatter(x21,-cp21,label='Deformed')
plt.grid()
plt.xlabel('x')
plt.ylabel('Cp')
plt.legend()
plt.title('Cp Plot')

plt.figure(figsize=(20,16))
plt.scatter(x3,-cp3,label='Initial')
plt.scatter(x31,-cp31,label='Deformed Down')
plt.scatter(x32,-cp32,label='Deformed Up')
plt.grid()
plt.xlabel('x')
plt.ylabel('Cp')
plt.legend()
plt.title('Cp Plot')

plt.figure(figsize=(20,16))
plt.scatter(x4,-cp4,label='Initial')
plt.scatter(x41,-cp41,label='Deformed Down')
plt.scatter(x42,-cp42,label='Deformed Up')
plt.grid()
plt.xlabel('x')
plt.ylabel('Cp')
plt.legend()
plt.title('Cp Plot')

plt.show()