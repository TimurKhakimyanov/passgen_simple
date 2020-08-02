#Программа для генерации пароля очень простая все буквы латинские
#Для использования просто введите желаемую длину пароля далле программа выведет пароль
#August 2, 2020 
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from random import choice
chars = ascii_letters + digits
passgen = 0
print("введите желаемую длину пароля")
n = int(input())
passgen = ''.join(choice(chars) for _ in range(n))
print(passgen)

