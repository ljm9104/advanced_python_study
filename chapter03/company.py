#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author:    LJM
# @Date:      2018-04-20 14:13:12
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    
    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

    # def __str__(self):
    #     return ",".join(self.employee)

    # def __repr__(self):
    #     return ".".join(self.employee)

company = Company(["tom", "bob", "jane"])
print(company)  # <__main__.Company object at 0x0000000000BC2940>
print(company[:]) 

# company1= company[:2]
# print(len(company))
# for em in company1:
#     print(em)