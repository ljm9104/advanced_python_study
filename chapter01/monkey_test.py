# -*- coding: utf-8 -*-
class Student:
    def say(self):
        print("i am student")


def say_teacher():
    print("i am teacher")


stu = Student()
stu.say = say_teacher
stu.say()
