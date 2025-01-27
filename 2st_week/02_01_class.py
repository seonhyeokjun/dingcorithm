class Person:
    def __init__(self, param_name):
        print("hihihi", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요 저는", self.name, "입니다")


person_1 = Person("유재석")  # hihihi <__main__.Person object at 0x1067e6d60> 이 출력됩니다!
print(person_1.name)  # 유재석
person_1.talk()  # 안녕하세요 저는 유재석 입니다

person_2 = Person("박명수")  # # hihihi <__main__.Person object at 0x106851550> 이 출력됩니다!
print(person_2.name)  # 박명수
person_2.talk()  # 안녕하세요 저는 박명수 입니다