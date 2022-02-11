x=input("x: ")
y=input("y: ")
z=input("z: ")
zs=input("Value: ")

x=int(x)
y=int(y)
z=int(z)

f_out=open("DV_Value.txt", 'w')
zs=float(zs)

for k in range(z+1):
    zi = zs
    for j in range(y+1):
        #if j==0:
         #   zi=0
        for i in range(x+1):
            if k==z and j==y and i==x:
                f_out.write(str(zi))
            else:
                f_out.write(str(zi) + ", ")
        if j==0:
            zi=zs
        else:
            #zi *= 1.5
            zi=zi

f_out.close()