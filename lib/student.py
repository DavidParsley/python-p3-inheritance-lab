#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []
    
    def learn(self, added_knowledge):
        return self.knowledge.append(added_knowledge)
    
david = Student("David", "Parsley")
print(david.first_name, david.last_name)
david.learn("Houston,We Have A Problem ! ") 
print(david.knowledge)
        
parsley = Student("Parsley", "David")
print(parsley.first_name, parsley.last_name)
parsley.learn("Ankara Messi") 
print(parsley.knowledge)

third_wheeler = Student("Third", "Wheeler")
print(third_wheeler.first_name, third_wheeler.last_name)
print(third_wheeler.knowledge)

                