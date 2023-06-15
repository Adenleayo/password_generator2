import string
import random 

def generate_password():
    password= input('pls input your password: ')
    length = 0 
    if password == 'weak':
        length += 5
    elif password == 'strong':
        length += 8 
    elif password == 'very strong':
        length += 15
    else:
        print('pls input weak,strong,verystrong to generate random password')    
        
    save = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(save)for i in range(length))
    return password


new_password = generate_password()

print(f'this is your password  : {new_password}')       
        
               
