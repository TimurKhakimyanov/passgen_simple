#The password generation program is very simple all letters are Latin
#To use, just enter the desired password length and then the program will display the password
#Программа для генерации пароля очень простая все буквы латинские
#Для использования просто введите желаемую длину пароля далее программа выведет пароль
#August  2020 
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from random import choice
chars = ascii_letters + digits
passgen = 0
print("введите желаемую длину пароля")
n = int(input())
passgen = ''.join(choice(chars) for _ in range(n))
print(passgen)

