x=input("x: ")
y=input("y: ")
z=input("z: ")

x=int(x)
y=int(y)
z=int(z)

f_out=open("DV_Twist.txt", 'w')

#    FFD_TWIST              (  15, Scale | Mark. List | FFD_BoxTag, j_Ind, x_Orig, y_Orig, z_Orig, x_End, y_End, z_End )

zi=0.0
scale=0.1
ys=1.7
ye=2
ydiff=(ye-ys)/y
for j in range(y+1):
    if j==y:
        f_out.write("( 15, " + str(scale) + " | flowboundwinglet, feaboundwinglet | WINGLET, " + str(j) + ", 1.2, "+str(ys)+", 0.0, 1.2, 5.0, 0.0 )")
        #f_out.write("( WINGLET, " + str(j) + ", 1.2, " + str(ys) + ", 0.0, 1.2, 5.0, 0.0 )")
    else:
        f_out.write("( 15, " + str(scale) + " | flowboundwinglet, feaboundwinglet | WINGLET, " + str(j) + ", 1.2, "+str(ys)+", 0.0, 1.2, 5.0, 0.0 ); ")
        #f_out.write("( WINGLET, " + str(j) + ", 1.2, " + str(ys) + ", 0.0, 1.2, 5.0, 0.0 ); ")
    if j!=0:
        zi+=1.0
        scale += 0.1
        #scale=scale
        zi = round(zi, 1)
        scale = round(scale, 5)
    else:
        zi=zi
        scale=scale
    ys+=ydiff
    ys = round(ys, 5)


f_out.close()