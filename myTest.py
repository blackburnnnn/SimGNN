# -*- coding: UTF-8 -*-
import torch
import numpy as np
import argparse
import json
import math
from texttable import Texttable


class Person(object):
    def __init__(self, name, gender, age):
        self.name = "123"
        self.gender = gender
        self.age = age


class Student(Person):
    def __init__(self, name, gender, age, school, score):
        super(Student, self).__init__(name,gender,age)
        # super().__init__(name, gender, age)
        self.name = name.upper()
        self.gender = gender.upper()
        self.school = school
        self.score = score


s = Student('alice', 'female', 18, 'Middle school', 87)
print(s.school)
print(s.name)