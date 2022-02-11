x=input("x: ")
y=input("y: ")
z=input("z: ")

x=int(x)
y=int(y)
z=int(z)

f_out=open("DV_Def3.txt", 'w')
for k in range(z+1):
    for j in range(y+1):
        for i in range(x+1):
            if j==0:
                f_out.write("( 11, 0.2 | flowbound, feabound | WINGLET, " + str(i) + ", " + str(j) + ", " + str(k) + ", 0.0, 0.0, 1.0 ); ")
            elif j == 1:
                f_out.write("( 11, 0.5 | flowbound, feabound | WINGLET, " + str(i) + ", " + str(j) + ", " + str(k) + ", 0.0, 0.0, 1.0 ); ")
            else:
                f_out.write("( 11, 1.0 | flowbound, feabound | WINGLET, " + str(i) + ", " + str(j) + ", " + str(k) + ", 0.0, 0.0, 1.0 ); ")

f_out.close()
