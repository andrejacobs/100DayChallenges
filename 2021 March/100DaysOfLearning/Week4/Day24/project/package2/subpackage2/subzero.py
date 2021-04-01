# subzero.py
import sys
print(f'{__name__} sys.path: {sys.path}')

# This will throw ImportError: attempted relative import beyond top-level package
#from ...package1.hello import say_hello

print('subzero.py will import package1/hello.py absolutely')
from package1.hello import say_hello

say_hello('subzero')
