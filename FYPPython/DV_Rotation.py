x=input("x: ")
y=input("y: ")
z=input("z: ")

x=int(x)
y=int(y)
z=int(z)

xs=0.85
xe=1.3
ys=1.8
ye=1.95
zs=-0.1
ze=0.1
xdiff=(xe-xs)/x
ydiff=(ye-ys)/y
zdiff=(ze-zs)/z

f_out=open("DV_Rotation.txt", 'w')
#    FFD_ROTATION           (  18, Scale | Mark. List | FFD_BoxTag, x_Axis, y_Axis, z_Axis, x_Turn, y_Turn, z_Turn )
for k in range(z+1):
    zi=0.1
    for j in range(y+1):
        xsi = xs
        for i in range(x+1):
            if k==z and j==y and i==x:
                #f_out.write("( 18, " + str(scale) + " | flowboundwinglet, feaboundwinglet | WINGLET, 1.0, 1.8, 0.0, 0.0, 0.0, " + str(zi) + " )")
                f_out.write("( WINGLET, "+str(xsi)+", 1.8, 0.0, 1.0, 0.0, 0.0 )")
            else:
                #f_out.write("( 18, " + str(scale) + " | flowboundwinglet, feaboundwinglet | WINGLET, 1.0, 1.8, 0.0, 0.0, 0.0, " + str(zi) + " ); ")
                f_out.write("( WINGLET, "+str(xsi)+", 1.8, 0.0, 1.0, 0.0, 0.0 ); ")
            xsi+=xdiff
            xsi = round(xsi, 4)

        if j!=0:
            zi+=0.1
            zi = round(zi, 4)
        else:
            zi=zi

#f_out.write("\n")
#f_out.write("\n")
#for k in range(z+1):
#    zi=0.1
#    scale=1.0
#    for j in range(y+1):
#        for i in range(x+1):
#            if k==z and j==y and i==x:
#                #f_out.write("( 18, " + str(scale) + " | flowboundwinglet, feaboundwinglet | WINGLET, 1.0, 1.8, 0.0, 0.0, 0.0, " + str(zi) + " )")
#                f_out.write("FFD_ROTATION")
#            else:
#                #f_out.write("( 18, " + str(scale) + " | flowboundwinglet, feaboundwinglet | WINGLET, 1.0, 1.8, 0.0, 0.0, 0.0, " + str(zi) + " ); ")
#                f_out.write("FFD_ROTATION, ")


f_out.close()
