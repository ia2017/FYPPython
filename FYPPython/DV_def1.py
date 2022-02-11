x=input("x: ")
y=input("y: ")
z=input("z: ")

x=int(x)
y=int(y)
z=int(z)

f_out=open("DV_Def1.txt", 'w')
for k in range(z+1):
    for j in range(y+1):
        for i in range(x+1):
            if k==z and j==y and i==x:
                f_out.write("( 100, 0.1 | flowbound, feabound | WINGLET, " + str(i) + ", " + str(j) + ", " + str(k) + " )")
            else:
                f_out.write("( 100, 0.1 | flowbound, feabound | WINGLET, " + str(i) + ", " + str(j) + ", " + str(k) + " ); ")

f_out.close()
