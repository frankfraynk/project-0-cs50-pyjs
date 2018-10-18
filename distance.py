import math as m
def distance(x1,y1,x2,y2):
    xdel=(x2-x1)**2
    ydel=(y2-y1)**2
    dist = m.sqrt(xdel+ydel)
    return dist
xl = []
yl = []
dists = []
while True:
    ux = input("X for coordinate (blank for exit): ")
    if ux == "":
        break
    ux = int(ux)
    uy = int(input("Y for coordinate: "))
    xl.append(ux)
    yl.append(uy)
for i in range(len(xl)-1):
        x2 = xl[i+1]
        y2 = yl[i+1]
        dist = distance(xl[i],yl[i],x2,y2)
        dists.append(float(dist))        
perimeter = sum(dists)
print(perimeter, "is your perimeter")
