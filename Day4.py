units=int(input("Enter units:"))
amount=0
if units>0:
    if units<=100:
        amount=units*5
    elif units<=300:
        amount=100*5 + (units-100)*7
    else:
        amount=100*5 + 300*7 + (units-400)*10
else:
    print("Invalid units")

if amount>5000:
    amount-=amount*0.05

print(amount)





user_input = ('Hello','Hi',20,40.2,9.6j,[1,2],'PYTHON','JECRC',(1,2,3))
new_coll = {}

for i in user_input:
    if type(i) in [tuple,str,set]:
        l=len(i)
        if l%2==0:
            new_coll[i]=i[0]+i[-1]
        else:
            mid=i[l//2]
            new_coll[i]=mid

print(new_coll)















# for i in user_input:

#     if(type(i) in [str,tuple,set]):
#         l = len(i)
#         if(l%2==0):
#             new_coll[i] = i[0]+i[l-1] 
#         else:
#             new_coll[i] = i[l//2]

# print(new_coll)




#Loan approval

salary=int(input("Enter salary: "))
cibil_score=int(input("Enter cibil score: "))

if salary>25000 and cibil_score>700:
    if salary>50000 and cibil_score>750:
        print("instant approval")
    else:
        print("approved")
else:
    print("rejected")





    #wap program to check a year is leap or not

year=int(input("Enter the year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("Leap year")
else: 
    print("Not leap year")




    #WAP to take a character from the user and convert it into lowercase if its in uppercase or vice-versach=input()val=ord(ch)if val>=65 and val<=90:    ch=chr(val+32)elif (val>=97 and val<=122):    ch=chr(val-32)print(ch)# if ch.islower():#     print(ch.upper())# else:#     print(ch.lower())
#WAP to take a character from the user and convert it into lowercase if its in uppercase or vice-versa

ch=input()
val=ord(ch)

if val>=65 and val<=90:
    ch=chr(val+32)
elif (val>=97 and val<=122):
    ch=chr(val-32)

print(ch)

# if ch.islower():
#     print(ch.upper())
# else:
#     print(ch.lower())




#WAP to print 1 to 5 using while loop

num=1
while(num<6):
    print(num)
    num+=1




#wap to achieve desired output for the below given output
#Hello123@ --> hELLO123@

string=input("Enter a string: ")
l=len(string)-1
st=0
result=''

while(st<=l):
    
    char=string[st]
    val=ord(char)
    if 'A'<=char<='Z':
        ch=chr(val+32)
    elif 'a'<=char<='z':
        ch=chr(val-32)
    else:
        ch=char
    result+=ch
    st+=1

print(result)




#WAP to find out the maximum number 

l=[10,2.2,5,"Hello",[100,2000],99.0]
st=0
length=len(l)-1
max=float('-inf')
while(st<=length):
    if(type(l[st]) in [int,float]):
        if max<l[st]:
            max=l[st]
    st+=1
print(max)



# dict={1:11,2:22}

# for key, value in dict.items():
#     print(key,value)

dict={'a':1,'b':2,'c':3,'d':4}
new_dict={}

for index in dict:
    new_dict[dict[index]]=index

print(new_dict)