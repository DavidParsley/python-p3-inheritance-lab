from user import User

import random

class Teacher(User):

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

    def teach(self):
        if len(self.knowledge) > 0:
            return random.choice(self.knowledge)
        else:
            print("No Knowledge")

simon= Teacher("Simon", "Luuu")
print(simon.first_name, simon.last_name)
print(simon.teach())