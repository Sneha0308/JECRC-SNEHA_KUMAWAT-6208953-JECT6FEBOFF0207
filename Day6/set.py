s1 ={1,2,3}
s2 ={2,3,4}
# s3 =s1.union(s2)
# print(s3)

# s1.intersection(s2)
# print(s1)
# print(s2)

s1.difference(s2)
print(s1)



## get()

d= {1:1,2:2,3:3,(1,2,3):(1,2,3)}

d.get(2)
print(d)


# d.get(1,2,3)
# d[1]
# print(d)




user= {'username' :'user123' , 'password':'******' }
# user.pop('loaction')
print(user)

# pop
user.pop('usename','password')
print(user)

# popitem 
user.popitem()
print(user)

# update

user2 = {'username' :'user123' , 'password':'******' }
user2['password'] = '123'
print(user2)

# inside of it we  shuld pass one directonary
#  create a function which will take n number of inputs from the user and return the sum of only int & floting point numbers .make sure user is capable of passing all types\ f values


def add_nums(*args):
    print(args,type(args))
    sum = 0
    for i in args:
    # for insntance(i,(int,float))
        if  type(i) in (int,float) :
            sum += i
    print(f'Addition : {sum}')        
add_nums()
add_nums(1,2,3,4,'hello','hiii')   






# def func_name(**):
#   statement
# block

# func_name(k1=v1,k2=v2,...k,kn=vn)
# all the key name should  a string but you cant use quotes

# def print_details(**kwargs):
#     print(kwargs)

# print_details(username = 'user123',password ='****')    




# create a function which will return a list of prime numbers.make sure can pass n of inputs .for cheking wheter a number is prime or not,u can crete one function

def isprime(num):
    if num < 2:
        return False
    else:
    
         for i in range(2, num):
         
             if num % i == 0:
              return False
            
         return True


def find_prime_nums(*args):
    prime = []
    for num in args:
        if isprime(num):
            prime.append(num)
    
            
    return prime

print(find_prime_nums(*eval(input('eater a list of nums:'))))
    


