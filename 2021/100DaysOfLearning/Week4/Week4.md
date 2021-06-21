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

### Day 23: 31 March 2021

**Today**: Explored a bit more on how the Python importing process works.

**Thoughts:** Unrelated to the learning process, but today we received a shocking phone call from nursery to tell us that our 1.5 year old daughter managed to escape nursery! Luckilly nothing happened to her.

**Key concepts:**

1. Stop thinking about where Python files are located. It is all about how the system searches and loads modules.
2. Python imports are case-sensitive. import koos != import Koos
3. sys.path is mega important.
4. When a script is run (python module.py) then sys.path[0] is the directory that contains the script. I.e. not the current working directory.
5. sys.path is shared across all the imported modules.
6. sys.path can be modified.
7. Built-in modules are found first and then sys.path is consulted.

**Links:**

1. [Day 23 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-23-more-exploring-of-the-python-importing-process/)

---

### Day 24: 1 April 2021

**Today**: Wrapping up my current journey of understanding the Python importing process.

**Thoughts:** Happy April Fools day

**Key concepts:**

1. pkgutil.iter_modules can be used to find all available modules.
2. Absolute imports are preferred over relative imports.
3. Absolute imports uses the full path from the project's root directory to the module to be imported.
4. Relative imports uses the relative path from the current module to the module to be imported.

**Links:**

1. [Day 24 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-24-wrapping-up-on-the-python-importing-process/)
2. [Real Python tutorial](https://realpython.com/python-modules-packages/)
3. [Real Python advanced tutorial](https://realpython.com/python-import/)
4. [Check if a module has been imported](https://stackoverflow.com/questions/30483246/how-to-check-if-a-python-module-has-been-imported)

---

### Day 25: 2 April 2021

**Today**: Watched a stream about containers on arm from Alex Ellis and Bret Fisher. Also watched the creator of php talk about 25 years of php.

**Thoughts:** ARM is everywhere now and v9 is going to be worth keeping an eye on.

Php propped up on the intowebs this week because of the supply chain attack to their git repo. Somehow I came across the creator's talk about the last 25 years of php.

A lot of people have a hate for php, but they got to realize that probably most of the modern web would not be what we have now if it was not for php. I built my first website in 1996 using just html and I still recall having fond memories when I later discovered php. Also at the time the nearest competitor was ASP 1 and that just totally sucked!

I still dabble in php on the very odd occassion and that would mainly be for WordPress.

**Key concepts:**

1. Some times you just got to build the software that you would like to have.
2. But don't for one moment think that it means there is a market and you are going to get rich of it.

**Links:**

1. [25 years of php](https://www.youtube.com/watch?v=wCZ5TJCBWMg&t=1748s)
2. [Containers on arm platforms with Alex Ellis: DevOps and Docker Live Show (Ep 118)](https://www.youtube.com/watch?v=xBl67nmrTOI&t=3s)
3. [Bret Fisher's courses](https://www.bretfisher.com/courses/)

---

### Day 26: 3 April 2021

**Today**: Today I setup a headless Raspberry Pi Zero W.

**Thoughts:** Turns out today is my first public contribution to [open source](https://github.com/joemasilotti/HTTP-Client).

**Key concepts:**

n/a

**Links:**

1. [Day 26 blog post](https://andrejacobs.org/100-days-challenge/setting-up-a-headless-raspberry-pi-zero-w-with-raspberry-pi-os-lite/)
2. [Build a Timelapse Rig with your Raspberry Pi](https://blog.alexellis.io/raspberry-pi-timelapse/)
3. [Phototimer software](https://github.com/alexellis/phototimer)
4. [Pimoroni Headless Pi](https://learn.pimoroni.com/tutorial/sandyj/setting-up-a-headless-pi)
5. [First public open source contribution](https://twitter.com/joemasilotti/status/1378356813159010315)

---

### Day 27: 4 April 2021

**Today**: Learning about different hydroponic techniques.

**Thoughts:** I have now done 1 month of Learning every day!

**Key concepts:**

1. Aquaponics is the combination of aquaculture (fish) and Hydroponics.
2. NFT (Nutrient Film Technique) is the more classic hydroponics that come to mind. The nutrient water is run in a channel with a slight slope and the plants "float" on top of the nutrien film.
3. DWC (Deep Water Culture). A container filled with the nutrient water and an airstone placed inside. The roots are submerged in the water.
4. Ebb and Flow. The plants are placed in a medium (clay pebbles, coco etc.) and the container is flooded a few times during the day with the nutrient water and then allowed to drain back to the reservoir.
5. Drip system. The nutrient water is pumped to the plants and dripped at a constant rate into the plant containers and then drains back to the reservoir.
6. Aeroponics. Almost the same as DWC, but the nutrient water is sprayed / misted at the top where the roots are.
7. Kratky method. Plants in a jar with nutrient water, simples.
8. Dutch Bucket System. Basically the drip system.

**Links:**

1. [Different types hydroponics systems](https://www.nosoilsolutions.com/6-different-types-hydroponic-systems/)
2. [Dutch bucket for indoors](https://momsindoorgarden.com/2019/06/18/dutch-bucket-for-indoor-vegetable/)

---
