class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
    def move(self):
        print("move move!")

class Dog(Animal):  # 상속받음, 다중 상속 가능
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):  # 오버라이딩
        print("bark bark!!")
class Duck(Animal):
    def speak(self):
        print("quack!! quack!!")

dog1 = Dog("라이코스", "닥스훈트")
dog2 = Dog("바미", "보리콜리")
duck1 = Duck("도날드")
dog1.speak()
dog2.speak()
duck1.speak()

print(dog1.name, dog2.name, duck1.name)
