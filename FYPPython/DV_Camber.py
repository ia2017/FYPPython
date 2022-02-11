x=input("x: ")
y=input("y: ")
z=input("z: ")

x=int(x)
y=int(y)
z=int(z)

f_out=open("DV_Camber.txt", 'w')

#    FFD_TWIST              (  15, Scale | Mark. List | FFD_BoxTag, j_Ind, x_Orig, y_Orig, z_Orig, x_End, y_End, z_End )

zi=0.0
#scale=0.1
ys=1.81
ye=2.2
ydiff=(ye-ys)/y


for i in range(x+1):
    scale = 0.1
    for j in range(y+1):
        if i==x and j==y:
            f_out.write("( 14, " + str(scale) + " | flowbound, feabound | WINGLET, " + str(i) + ", " + str(j) + " )")
            #f_out.write("( WING, " + str(j) + " )")
        else:
            f_out.write("( 14, " + str(scale) + " | flowbound, feabound | WINGLET, " + str(i) + ", " + str(j) + " ); ")
            #f_out.write("( WING, " + str(j) + " ); ")
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
