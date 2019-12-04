class Triangle : 
    cal_count = 0
    
    def __init__(self, b, h = 5) :
        self.b = b
        self.h = h
        
    def area(self) :
        Triangle.cal_count += 1
        
        return self.b * self.h / 2
    
    @staticmethod
    def isIsosceles(a, b) :
        Triangle.cal_count += 1
        return a == b
    
    @classmethod
    def printCount(cls) :
        print(cls.cal_count)
   
tri1 = Triangle(4) #및변 4 삼각형 객체 생성

print(tri1.b, tri1.h, tri1.area(), tri1.cal_count)
print(Triangle.isIsosceles(5,4))

tri1.printCount() #인스턴스로 접근
Triangle.printCount() #클래스로 직접 접근
print(Triangle.cal_count)
