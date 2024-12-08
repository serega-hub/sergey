import random

elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_lengts = int(input('Введите длину пароля: '))

password = ''

for i in range(pass_lengts):
    password +=random.choice(elements)

print("Ваш пароль: " + password)
