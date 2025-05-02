class Rectangle:
        count = 0 # 클래스 변수
        def __init__(self,w,h):
            self.width = w
            self.height = h
        # 인스턴스 메서드(기본)
        def calcAraa(self):
            # self 사용 가능
            return self.width * self.height

        @staticmethod
        def isSquare():
            # 단순 기능
            print("정적 메서드")

        @classmethod
        def printCount(cls):
            # cls 클래스 변수 접근 가능
            cls.count += 1
            print(cls.count)

# 인스턴스 생성
obj = Rectangle(10, 20)
obj2 = Rectangle(60, 100)
# 인스턴스 메서드 사용가능
print(obj.calcAraa())
print(obj2.calcAraa())
# Rectangle.calcAraa() 오류남
Rectangle.isSquare() # 정적메서드는 class. 으로 사용 가능
Rectangle.printCount() # 클래스 메서드도 class. 으로 사용 가능(클래스 변수 사용 가능)
