'''
-- phenomena to making the operator to work on user-defined data types by invoking magic methods.
-- magic method means in which double underscore will bw there at the starting and ending 

--Example:
1.__add__,
2.__sub__,
3.__mul__,
4.__floordiv__,
5.__truediv__,
6.__mod__;

-- if we dont use oo then what will happeen
--For using the oprator inside user defined datatype we have to use it

--Syntax:
   class ClassName:
       def__init__(self,val):
          self.val = val

        def__add__(self,ano_obj):
           return self.val + ano_obj.val

    obj1= ClassName(val1) 
    obj2= ClassName(val2)     
    print(obj1 + obj2) ## obj1.__add__(obj2)

'''

class MyDT:
    def __init__(self,val):
        self.val = val

    def __str__(self):
        return  str(self.val)
    
    def __add__(self,*ano_obj):
        sum= self.val
        for i in ano_obj:
            sum += i.val
        return MyDT(sum)    

    # def add(self,*args):
    #     sum = self.val
    #     for i in args:
    #         sum += i.val
    #     return sum    
       
    def __sub__(self,ano_obj):
        return self.val - ano_obj.val
    def __mul__(self,ano_obj):
        return self.val * ano_obj.val
    def __floordiv__(self,ano_obj):
        return self.val // ano_obj.val
    def __truediv__(self,ano_obj):
        return self.val % ano_obj.val
    
# print(MyDT(10.10) + MyDT(20))
# print(MyDT .add(MyDT(100),MyDT(200),MyDT(300),MyDT(400)))


print(MyDT(100)- MyDT(20))    
print(MyDT(10)* MyDT(20))    
print(MyDT(100)//MyDT(20))    
print(MyDT(100) / MyDT(20))    

    
  
