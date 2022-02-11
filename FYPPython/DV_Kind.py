x=input("x: ")
y=input("y: ")
z=input("z: ")
kind=input("Kind: ")

x=int(x)
y=int(y)
z=int(z)

f_out=open("DV_Kind.txt", 'w')

for k in range(z+1):
    for j in range(y+1):
        for i in range(x+1):
            if k==z and j==y and i==x:
                f_out.write(kind)
            else:
                f_out.write(kind + ", ")

f_out.close()