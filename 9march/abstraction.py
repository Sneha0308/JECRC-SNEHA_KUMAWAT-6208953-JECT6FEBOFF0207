'''
Astraction :hiding the internal implementation and showing only functionality to the end user.

Abstract method:only function declation not defination 
                 
Abstarct class: if a class consist of at least one abstract method 

concret class: if a class doent have a single abs. method
abc: Module
ABC : Abstract BAse Class

'''

from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_bal(self):
        pass

    @abstractmethod
    def deposite(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

obj = ATM()

class SBI_ATM(ATM):
    def genrate_pin(self):
        print('it is used to generate atm pin')

    def forget_pin(self):
        print('not able to remember the pin! then forget now!')

    def check_bal(self):
        print('no balance is there')

    def deposite(self):
        print('save your money by giving it to me !')

    def withdraw(self):
        print('do not withdraw the monwy! pleas')

obj =SBI_ATM()
obj.generate_pin()
obj.forget_pin()
obj.check_bal()
obj.deposite()
obj.withdraw()         