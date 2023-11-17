#Password generator
import random

Password = ""
PassChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=|\;:<,>.?/'

Len = random.randint(1, 15)

for i in range(Len):
    Password += random.choice(PassChars)

print(Password)