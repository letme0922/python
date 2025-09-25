# 사람을 나타내는 가장 기본적인 클래스예요.
# 모든 사람은 번호(id)와 이름(name)을 가지고 있어요.
class Person:
    # 새로운 사람을 만들 때는 번호와 이름이 필요해요
    def __init__(self, id, name):
        self.id = id        # 사람의 번호를 저장해요
        self.name = name    # 사람의 이름을 저장해요
    
    # 이 사람의 정보를 화면에 보여주는 기능이에요
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

# 관리자는 일반 사람인데, 직책(title)이 추가로 있어요
# 예를 들면 '팀장님', '부장님' 같은 직책이에요
class Manager(Person):
    # 새로운 관리자를 만들 때는 번호, 이름, 직책이 필요해요
    def __init__(self, id, name, title):
        super().__init__(id, name)  # 먼저 일반 사람처럼 번호와 이름을 저장해요
        self.title = title          # 그리고 직책도 저장해요
    
    # 관리자의 정보를 화면에 보여주는 기능이에요
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")

# 직원은 일반 사람인데, 특별한 기술(skill)이 추가로 있어요
# 예를 들면 '파이썬', '자바' 같은 컴퓨터 기술이에요
class Employee(Person):
    # 새로운 직원을 만들 때는 번호, 이름, 기술이 필요해요
    def __init__(self, id, name, skill):
        super().__init__(id, name)  # 먼저 일반 사람처럼 번호와 이름을 저장해요
        self.skill = skill          # 그리고 기술도 저장해요
    
    # 직원의 정보를 화면에 보여주는 기능이에요
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")

# 여기서부터는 우리가 만든 클래스들이 잘 작동하는지 확인하는 테스트 코드예요
if __name__ == "__main__":
    # 테스트 1: 일반 사람을 만들어볼까요?
    print("=== 일반 사람 테스트 ===")
    person = Person("P001", "홍길동")
    person.printInfo()

    # 테스트 2: 관리자를 만들어볼까요?
    print("\n=== 관리자 테스트 ===")
    manager = Manager("M001", "김부장", "개발팀장")
    manager.printInfo()

    # 테스트 3: 직원을 만들어볼까요?
    print("\n=== 직원 테스트 ===")
    employee = Employee("E001", "이사원", "Python")
    employee.printInfo()

    # 테스트 4: 여러 명의 일반 사람들을 한번에 만들어볼까요?
    print("\n=== 여러 명의 일반 사람 테스트 ===")
    people = [Person("P002", "강감찬"), Person("P003", "이순신")]
    for p in people:
        p.printInfo()

    # 테스트 5: 여러 명의 관리자를 만들어볼까요?
    print("\n=== 여러 명의 관리자 테스트 ===")
    managers = [
        Manager("M002", "박과장", "프로젝트 매니저"),
        Manager("M003", "최부장", "기술이사")
    ]
    for m in managers:
        m.printInfo()

    # 테스트 6: 여러 명의 직원을 만들어볼까요?
    print("\n=== 여러 명의 직원 테스트 ===")
    employees = [
        Employee("E002", "정개발", "Java"),
        Employee("E003", "송개발", "JavaScript")
    ]
    for e in employees:
        e.printInfo()

    # 테스트 7: 아무것도 적지 않은 사람도 만들 수 있어요
    print("\n=== 빈 정보 테스트 ===")
    empty_person = Person("", "")
    empty_person.printInfo()

    # 테스트 8: 특별한 글자가 들어간 이름도 사용할 수 있어요
    print("\n=== 특수문자 테스트 ===")
    special_person = Person("P#123", "김#길동")
    special_person.printInfo()

    # 테스트 9: 아주 긴 이름이나 직책도 사용할 수 있어요
    print("\n=== 긴 문자열 테스트 ===")
    long_manager = Manager(
        "M999999", 
        "김길동" * 5,  # 이름을 5번 반복해요
        "수석 아키텍트 엔지니어"
    )
    long_manager.printInfo()

    # 테스트 10: 다른 나라 글자로 된 이름도 사용할 수 있어요
    print("\n=== 다른 나라 글자 테스트 ===")
    multi_employee = Employee("E999", "スズキ", "AWS")
    multi_employee.printInfo()