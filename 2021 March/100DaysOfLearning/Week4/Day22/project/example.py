# example.py

print(f'This is global scope of example.py. __name__ is: {__name__}')
print(f'example.py __package__ is: {__package__}')

import module1
import package1

if __name__ == '__main__':
    print('This is example.py running')
    print(f'My __name__ is: {__name__}')
