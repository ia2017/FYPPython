x=input("x: ")
y=input("y: ")
z=input("z: ")

x=int(x)
y=int(y)
z=int(z)

f_out=open("DV_Def.txt", 'w')
for k in range(z+1):
    for j in range(y+1):
        for i in range(x+1):
            if k==z and j==y and i==x:
                f_out.write("( 11, 0.1 | flowbound, feabound, clamped | WING, " + str(i) + ", " + str(j) + ", " + str(k) + ", 0.0, 0.0, 1.0 )")
            else:
                f_out.write("( 11, 0.1 | flowbound, feabound, clamped | WING, " + str(i) + ", " + str(j) + ", " + str(k) + ", 0.0, 0.0, 1.0 ); ")

f_out.close()
