# 100 Days Of Learning

## Log book - Week 4

### Day 21: 29 March 2021

**Today**: Troubleshooted more than I would have liked too.

**Thoughts:** Today is a bit of a failure in my book. I did not manage to hit the mark on a feature I wanted to implement. Also I had to be honest with my self and park this for now because I simply just don't have the time to see this through.

I did however learn a lot and also what not to do when combining OpenFaaS and tasks workers.

**Key concepts:**

1. The RQ worker needs to have access to the Python code. (duh!)
2. It also needs to be able to access the module in the correct way. Correct directory etc. for Python to be able to load the code for the task to be executed.
3. faasd uses containerd (not actually Docker)
4. Your functions access services using the IP 10.62.0.1 and the "external" port 

**Links:**

1. [Day 20 & 21 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-20-21-you-win-some-you-lose-some/)

---

### Day 22: 30 March 2021

**Today**: Started learning just how exactly Python module loading works.

**Thoughts:** The loading process is not as clear cut as you would think. Seems this trips up even some of the more experienced Python coders when they let their guard down.

**Key concepts:**

1. A module is any .py source code file.
2. A package can be any directory.
3. A package needed a `__init__.py` before Python 3.3
4. The name of the module first loaded and executed by the Python interpreter will be set to `__main__` regardless of what the module’s actual file name is.
5. python example.py and python -m example does not do the exact same thing!
6. `__package__` contains the name of the package the module belongs too.
7. All code in `__init__.py` will be executed when a package is imported.

**Links:**

1. [Day 22 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-22-understanding-the-python-importing-process/)
2. [The Definitive Guide to Python import Statements](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html)
3. [Python docs](https://docs.python.org/3/reference/import.html)

---
