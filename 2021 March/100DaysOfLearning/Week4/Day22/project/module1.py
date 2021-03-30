# module1.py

print(f'This is global scope of module1.py. __name__ is: {__name__}')
print(f'module1.py __package__ is: {__package__}')

if __name__ == '__main__':
    print('This is module1.py running')
