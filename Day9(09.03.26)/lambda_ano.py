
#  lambda args: <exp_1> if <<cond>else <exp_2>


# wap to find the square of a number if it is even.

# num = int(input('enter a number'))
# if num % 2==0:
#     print(num**2) 

result =lambda num : print(num**2)if num%2 == 0 else None
result(11)    


#  wap to find the sqaure of a number if it is even otherwise print cube of it 

result = lambda num: print(num**2)if num%2 ==0 else  print(num**3)
result(8)


# chek whether a num is +ve or -ve or 0

# num = int(input())
# if num >0:
#     print('positive')

# else: 
#     if num<0:
#         print('negative')

#     else:
#         print('zero')



result =lambda num: print('pos') if num> 0 else print ('neg') if num <0 else print ('zero')               
result (3)
result(-9)
result(0)
result(int(input()))