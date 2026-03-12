'''
In this the properties will be derived from multipple parent class to a single child class.

'''

class Parent_1:
    a=23
class Parent_2:
    b=134
class Parent_3:
    c=1456
class Parent_4:
    d=4556
class child(Parent_1,Parent_2,Parent_3,Parent_4):
    pass
print(child.a,child.b,child.c,child.d)