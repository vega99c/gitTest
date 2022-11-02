# # 인스턴스간의 관계
# class Person :
#     name    = "person name"
#     age     = 18

#     def __init__(self,name) :
#         self.name = name

# # 클래스의 속성값 : person name, 18
# # print(Person.name)


# # # 인스턴스에서 값 변경
# # p_instant1 = Person("인스턴트1")
# # p_instant1.age = 20

# # # 인스턴스의 속성값 확인 : 인스턴스 1, 20
# # print(p_instant1.name)
# # print(p_instant1.age)


# # # 클래스의 속성값 확인 : person name, 18  -- 변경없음.
# # print(Person.name)
# # print(Person.age)

# print("------------------------------")

# p_instant1 = Person("인스턴트1")

# print(Person.name, Person.age)
# # person name, 18

# Person.age = 33

# print(Person.name, Person.age)
# # person name, 33

# print(p_instant1.name, p_instant1.age)
# # 인스턴트1, 33

# 부모 클래스
class GrandMother :

    family = "grandparents"
    
    def print_self(self) :
        print(self)
    
    def print_HI():
        print("HI!")
        
# 자식 클래스
class father(GrandMother) :
    FAMILY = "parents"

    def __init__(self,name,age) :
        self.name = name
        self.age  = age
        self.home = "seoul"
        
father.print_HI() # HI! 작동함.

father1 = father("test1", 30)

print(father1.name, father1.age, father1.home)
father1.name = "wow"
father1.age = 55
father1.home = "no"
print(father.FAMILY)
father.FAMILY = "good"
print(father1.name, father1.age, father1.home)
print(father.FAMILY)

father2 = father('one',22)
print(father2.name)
print(father2.age)