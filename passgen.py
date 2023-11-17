#Password generator
import random

Password = ""
PassChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=|\;:<,>.?/'

Len = random.randint(8, 25)

for i in range(Len):
    Password += random.choice(PassChars)

print(Password)