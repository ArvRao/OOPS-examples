class Triangle:
    import math

    def __init__(self, a, b, c):
            self.a=a
            self.b=b
            self.c=c
    def area(self):
            s=(self.a+self.b+self.c)/2
            area=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
            return area
    
    def perimeter(self):
        p = self.a + self.b + self.c
        return p

    def show(self):
        return f'Triangle  with sides are {self.a} {self.b} {self.c}'

t1 = Triangle(2,5,3)
t2 = Triangle(8,1,4)

print(t1.show())