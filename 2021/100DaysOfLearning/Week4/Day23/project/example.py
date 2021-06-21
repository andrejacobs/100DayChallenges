# example.py
import sys

print(f'This is global scope of example.py. __name__ is: {__name__}')
print(f'example.py __package__ is: {__package__}')

import module1
import package1

# This should import the built-in and not the time.py module
import time

import package1.hello

sys.path.append('/Users/andre/temp')
import tempmodule

if __name__ == '__main__':
    print('This is example.py running')
    print(f'My __name__ is: {__name__}')
    
    print(f'sys.path: {sys.path}')
