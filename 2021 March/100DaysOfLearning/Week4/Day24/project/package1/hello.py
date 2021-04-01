# hello.py
import sys
print(f'{__name__} sys.path: {sys.path}')

print('hello.py will import module1')
import module1
module1.say_something()

def say_hello(name):
    print(f'Hello {name}!')
