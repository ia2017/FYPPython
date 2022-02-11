x=input("x: ")
y=input("y: ")
z=input("z: ")

x=int(x)
y=int(y)
z=int(z)

f_out=open("DV_Def.txt", 'w')


for k in range(z+1):
    zi=0.1
    scale=1.0
    for j in range(y+1):
        for i in range(x+1):
            if k==z and j==y and i==x:
                f_out.write("( 11, " + str(scale) + " | flowboundwinglet, feaboundwinglet | WINGLET, " + str(i) + ", " + str(j) + ", " + str(k) + ", 0.0, 0.0, " + str(zi) + " )")
            else:
                f_out.write("( 11, " + str(scale) + " | flowboundwinglet, feaboundwinglet | WINGLET, " + str(i) + ", " + str(j) + ", " + str(k) + ", 0.0, 0.0, " + str(zi) + " ); ")
        if j!=0:
            zi+=0.1
            scale += 1.0
            zi = round(zi, 1)
            scale = round(scale, 5)
        else:
            zi=zi
            scale=scale


f_out.close()
