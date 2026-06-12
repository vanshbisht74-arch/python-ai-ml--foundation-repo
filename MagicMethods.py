
#------------------------MAGIC METHODS-------------------------
class Point:
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
        

    def distance_between_coordinates(self,other):
        return ((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod)**2)**0.5 
    
    def distance_from_origin(self):
        return self.distance_between_coordinates(Point(0,0))
    

class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    def __str__(self):
        return "{}x+{}y+{}=0".format(self.A,self.B,self.C)
    
        
    def point_on_line(line,point):
        if line.A*point.x_cod+line.B*point.y_cod+line.C==0:
            return "POINT LIE ON THE LINE"
        
        else:
            return "DOES NOT LIE IN THE LINE"
        
    def shortest_distance(line, point):
        return abs(line.A * point.x_cod + line.B * point.y_cod + line.C) / (line.A**2 + line.B**2) ** 0.5

p1=Point(1,1)
l1=Line(1,2,3)

print(l1.point_on_line(p1))