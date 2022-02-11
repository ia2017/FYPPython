x=input("x: ")
y=input("y: ")
z=input("z: ")

x=int(x)
y=int(y)
z=int(z)

f_out=open("DV_Defwinglet.txt", 'w')
for k in range(z+1):
    #for j in range(y+1):
    for i in range(x+1):
        if k==z and i==x:
            #f_out.write("( 11, 1.0 | flowboundwinglet, feaboundwinglet | WINGLET, " + str(i) + ", " + str(j) + ", " + str(k) + ", 1.0, 1.0, 0.0 )")
            #f_out.write("( WINGLET, " + str(i) + ", " + str(j) + ", " + str(k) + ", 0.8825, 1.0, 0.0 )")
            f_out.write("( WINGLET, " + str(i) + ", 10, " + str(k) + ", 0.8825, 1.0, 0.0 )")
        else:
            #f_out.write("( 11, 1.0 | flowboundwinglet, feaboundwinglet | WINGLET, " + str(i) + ", " + str(j) + ", " + str(k) + ", 1.0, 1.0, 0.0 ); ")
            #f_out.write("( WINGLET, " + str(i) + ", " + str(j) + ", " + str(k) + ", 0.8825, 1.0, 0.0 ); ")
            f_out.write("( WINGLET, " + str(i) + ", 10, " + str(k) + ", 0.8825, 1.0, 0.0 ); ")

f_out.close()
