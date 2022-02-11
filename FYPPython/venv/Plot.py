from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes(projection='3d')
SIZEPLT = 28
plt.rc('font', size=SIZEPLT)          # controls default text sizes
plt.rc('axes', titlesize=SIZEPLT)     # fontsize of the axes title
plt.rc('axes', labelsize=SIZEPLT)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SIZEPLT)    # fontsize of the tick labels
plt.rc('legend', fontsize=SIZEPLT)    # legend fontsize
plt.rc('figure', titlesize=SIZEPLT)  # fontsize of the figure title

#a=np.array([-0.0403, 0, -0.04836, 0.8463, 0, -0.04836, 1.209,1.2896, -0.04836, 0.6851, 1.2896, -0.04836, -0.0403, 0, 0.04836, 0.8463,0, 0.04836, 1.209,1.2896, 0.04836, 0.6851, 1.2896, 0.04836])

# ---------------- WING ------------------


# Opening NACA airfoil file
f_in=open('NACA2412dat.txt','r')
next(f_in)
length=len(f_in.readlines())
length=int(length)

# Defining arrays
xa=np.zeros(length)
za=np.zeros(length)
ya=np.zeros(length)
ya1=np.ones(length)
f_in.seek(0)
next(f_in)
index=0

# Splitting to x and y variables
for i in f_in:
    x=i.split()
    for j in range(len(x)):
         x[j]=float(x[j])
    xa[index]=x[0]
    za[index]=x[1]
    index=index+1

# 3 Dimensionalising

span=5
ya1=ya1*span

# ------------------ For FFD Box --------------------

#a=np.array([-0.05, 0, -0.0924,  1.05, 0, -0.0924,    1.05, 5.1, -0.0924,      -0.05, 5.1, -0.0924,      -0.05, 0.05, 0.1292, 1.05, 0.05, 0.1292, 1.05, 5.1, 0.1292,    -0.05, 5.1, 0.1292])
#deg=np.array([8, 2, 1])

a=np.array([-0.05, -0.05, -0.1, 1.05, -0.05, -0.1, 1.3, 1.9, -0.1, 0.85, 1.9, -0.1, -0.05, -0.05, 0.1, 1.05, -0.05, 0.1, 1.3, 1.9, 0.1, 0.85, 1.9, 0.1])


x=np.zeros(8)
y=np.zeros(8)
z=np.zeros(8)

for i in range(8):
    x[i]=a[3*i]
    y[i]=a[3*i+1]
    z[i]=a[3*i+2]


# ---- Plotting -------

# FFD
ax.scatter3D(x,y,z, 'green')

# Wing
#ax.scatter3D(xa,ya,za, color='gray', s=1)
#ax.scatter3D(xa,ya1,za, color='gray', s=1)
#ax.plot3D([xa[0], xa[0]],[ya[0], ya1[0]],[za[0], za[0]],'gray')
#ax.plot3D([xa[100], xa[100]],[ya[100], ya1[100]],[za[100], za[100]],'gray')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

f_in.close()

