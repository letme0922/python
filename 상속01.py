#부모 클래스(공통분모) 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        #f-string:포맷 스트링을 사용하면 변수명 전달 
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스 
class Student(Person):
    #덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모 클래스의 생성자 호출
        #Person.__init__(self, name, phoneNumber)
        super().__init__(name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #덮어쓰기 
    def printInfo(self):
        #f-string:포맷 스트링을 사용하면 변수명 전달 
        print(f"Info(Name:{self.name}, Phone Number: {self.phoneNumber}, Subject: {self.subject}, Student ID: {self.studentID})")

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "241234")
p.printInfo()
s.printInfo() #자식 클래스에서 재정의한 메서드 호출


