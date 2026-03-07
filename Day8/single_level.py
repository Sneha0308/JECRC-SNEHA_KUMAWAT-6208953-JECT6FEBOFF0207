# INHERITANCE

'''
1.Single Level
2.Multi-Level
3.Multiple
4.Hierarihical
5.Hybrid
'''


# Single level: we will have a parent and child class.also the properties will be derived only one time.
# parent class:from which we are going to derive the properties
class Parent:
    bank_balance ='54L'
    def __init__(self,members):
       self.members =members

    def desc(self):
        print('I am the parent class')

# Child class or sub class:in which we are going to derive the properties

class Child(Parent):
    def __init__(self,child_name,*args):
        super().__init__(args)
        self.child_name = child_name


#     pass
# print(Child.bank_balance

# obj=Child()
# print(Child.bank_balance)
# obj.desc()

# constructor chaining : Calling parent class's constructor from inside child class
obj = Child('sneha','MOM','DAD')
print(obj.child_name)
print(obj.members)
print(obj.bank_balance)
obj.desc()
