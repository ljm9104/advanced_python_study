# 自省是通过一定的机制查询到对象的内部结构
# __dict__
# dir()函数

class Person:
    """
    人
    """
    name = "user"

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

if __name__ == "__main__":
    user = Student("慕课网")

    #通过__dict__查询属性
    print(user.__dict__)
    print(user.name)
    user.__dict__["school_addr"] = "北京市"
    print(user.school_addr)
    print(user.__dict__)
    # print(Person.__dict__)
    # a = [1,2]
    # print(dir(a))

