import math

radius=int(input("radius : > "),base=10)
radius=radius+1
SX=int(input("Center point of X => : "),base=10)
SY=int(input("Center point of Y => : "),base=10)
Distance=0
Points=[]
Template=[]
for i in range(radius):
    Template.append(i)
    Points.append(round(math.sqrt(radius**2-Template[i]**2)))
Points.reverse()
for i in range(radius):

    print((SX-Points[i])*" "+"ZK"+Points[i]*" "+(SX+Points[i])*" "+"ZK")
    if Points[i] == radius:
        Points.reverse()
    print((SX-Points[i])*" "+"ZK"+Points[i]*" "+(SX+Points[i])*" "+"ZK")


#reconfigurable code!!!