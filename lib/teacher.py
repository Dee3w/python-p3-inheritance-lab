#!/usr/bin/env python

from user import User

import random

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):
       def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.knowledge = knowledge

    def teach(self):
           random_element = random.randint(0,7)
        return self.knowledge[random_element]