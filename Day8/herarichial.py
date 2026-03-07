## In this the propeerties will be derived from single parent class to multiple child class.

class Parent:
    gold='2kg'
    silver='10kg'
    no_of_flats=12

class SmallestBrother(Parent):
    name ='AKASH'

class ElderBrother(Parent):
    my_name='SHUBHAM'

class Sister(Parent):
    sis_name='SNEHA'

print(SmallestBrother.gold)  
print(ElderBrother.silver)
print(Sister.no_of_flats)            