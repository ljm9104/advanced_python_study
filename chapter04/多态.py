class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a dog")


class Duck(object):
    def say(self):
        print("i am a duck")


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    # def __len__(self):
    #     return len(self.employee)


company = Company(["tom", "bob", "jane"])
print(company,type(company))

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


# dog = Dog()


a = ["bobby1", "bobby2"]
b = ["bobby2", "bobby"]
name_tuple = ("bobby3", "bobby4")
name_set = set()
name_set.add("bobby5")
name_set.add("bobby6")
a.extend(name_tuple)                # extend()只要传递一个可迭代的对象就可以
a.extend("123")
a.extend(range(10))
print(a)
