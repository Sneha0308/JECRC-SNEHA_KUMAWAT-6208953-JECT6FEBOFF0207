#Write a program to check whether the username and password is correct or not. If correct print login successfully, if not , do nothing

user={
    'username':'user123',
    'password':'****'
}

uid=input("Enter username: ")
upass=input("Enter password: ")

if(uid==user['username'] and upass==user['password']):
    print("Login successful")
else:
    print("Password or username is incorrect")
print("Program got ended")

#if-else-elif statements
'''
1. if statement 
2. if else
3. elif
4. nested
'''

#if statement block is also called TSB (True statement block)
#else statement block is also called FSB (False statement block)


#Write a program in python to take a character from the user and check whether it is a vowel or consonant or digit or special character

'''
1. take a character from user
2. apply conditions one by one 
3. 
'''
val=input("Enter a character: ")

if val>='a' and val<='z' or val>='A' and val<='Z':
    if val.lower() in 'aeiou':
        print('vowel')
    else:
        print('consonant')
elif val>='0' and val<='9':
    print('digit')
else:
    print('special character')

    #Write a program to check whether a character is alphabet or not
ch=input("Enter character")

if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    print("Is alphabet")
else:
    print("is not")