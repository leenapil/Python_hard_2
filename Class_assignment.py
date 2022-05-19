class Student:
    def __init__(self, name, grade, student_number, sex, address, phone_number, year):
        self.name = name
        self.grade = grade
        self.student_number = student_number
        self.sex = sex
        self.address = address
        self.phone_number = phone_number
        self.year = year
    
    def introduce_name(self):
        print("이름은 {} 이다.".format(self.name))
    def introduce_grade(self):
        print("학년은 {} 이다.".format(self.grade))
    def introduce_student_number(self):
        print("학번은 {} 이다.".format(self.student_number))
    def introduce_sex(self):
        print("성별은 {} 이다.".format(self.sex))
    def introduce_address(self):
        print("주소는 {} 이다.".format(self.address))
    def introduce_phone_number(self): 
        print("전화번호는 {} 이다.".format(self.phone_number))

    while True:
        Class_name = str(input("객체 명을 입력하시오. (단,영문으로) : "))
        if Class_name == "종료":
            break
        name = str(input("이름을 입력하시오. (단,한글로) : "))
        grade = int(input("학년을 입력하시오. (단,숫자로) : "))
        student_number = int(input("학번을 입력하시오. (단,숫자로) : "))
        sex = str(input("성별을 입력하시오. (모를 땐 모른다 라고 입력) : "))
        if sex == "모른다":
            print("None")
        address = str(input("주소를 입력하시오. (~시까지만) : "))
        phone_number =  input("전화번호를 입력하시오. (모를 땐 모른다 라고 입력) : ")
        if phone_number == "모른다":
            print("None")
        year = int(input("멋사 몇년차인가요? (단,숫자로) : "))
        print("이름은 {} 이다.".format(name))
        print("학년은 {} 이다.".format(grade))
        print("학번은 {} 이다.".format(student_number))
        print("성별은 {} 이다.".format(sex))
        print("주소는 {} 이다.".format(address))
        print("전화번호는 {} 이다.".format(phone_number))
        if year == 1:
            print("멋사 1년차")
            print("우와 아기사자다 !")
        else:
            print("멋사 {}년차".format(year))
            print("우와 운영진이다 !")
        
        

        # 한 줄 띄울게요
        print()