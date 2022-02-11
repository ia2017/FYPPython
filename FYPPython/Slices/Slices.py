from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f=open('wing_slices_unwinglet.dat','r')
#f=open('wing_slices_unwinglet.dat','r')
lines=f.readlines()[3:]
f.close()
nline=0
x=[]
y=[]
z=[]
xc=[]
yc=[]

for line in lines:
    num = ''
    i=0
    if line[0].isdigit()==True:
        for char in line:
            num=num+char
            if char == ' ':
                if i==0:
                    x.append(float(num))
                elif i==1:
                    y.append(float(num))
                elif i == 2:
                    z.append(float(num))
                elif i == 3:
                    xc.append(float(num))
                i+=1
                num=''
        yc.append(float(num))
    nline+=1

# Plotting
SIZEPLT = 28
plt.rc('font', size=SIZEPLT)          # controls default text sizes
plt.rc('axes', titlesize=SIZEPLT)     # fontsize of the axes title
plt.rc('axes', labelsize=SIZEPLT)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('legend', fontsize=SIZEPLT)    # legend fontsize
plt.rc('figure', titlesize=SIZEPLT)  # fontsize of the figure title

fig = plt.figure(1,figsize=(25,16),dpi=120)
ax = plt.axes(projection='3d')

ax.scatter3D(x,y,z, 'green')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_zlim(-0.2,0.2)

plt.show()