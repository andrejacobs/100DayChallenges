# 100 Days Of Learning

## Log book - Week 3

### Day 14: 22 March 2021

**Today**: Managed to get syntax highlighting working on my blog.

**Thoughts:** I really need to invest some more time in learning Docker so that I can use it to "freeze" a develop environment and that in theory I can just spin up containers in the future and everything "should" just work out of the box.

**Key concepts:**

Most of the key concepts was discovered yesterday.

**Links:**

1. [Day 13 & 14 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-13-14-running-wordpress-locally-using-docker-and-using-highlight-js/)
2. [highlight.js](https://highlightjs.org/)
3. [highlight.js demo](https://highlightjs.org/static/demo/)

---

### Day 15: 23 March 2021

**Today**: Learned about Phantom types in Swift. I also started exploring my options for downloading and storing images for the Lego database learning project.

**Thoughts:** I am more tired than usual today. Regardless I still managed to learn some new things.
Initially I was going to just do the stupid thing and store a BLOB in the database, but why do the simple and wrong thing when you can do the complex and hopefully right thing :-D

**Key concepts:**

1. Phantom type: a type that doesn’t use at least one of its generic type parameters.
2. It is used to build more type-safe APIs.
3. Schedule a function for OpenFaaS is literally just using cron to run faas-cli invoke. Simples.

**Links:**

Swift Phantom Types:

1. [Hacking with Swift](https://www.hackingwithswift.com/plus/advanced-swift/how-to-use-phantom-types-in-swift)
2. [Swift by Sundell](https://www.swiftbysundell.com/articles/phantom-types-in-swift/)
3. [Swift with Majid](https://swiftwithmajid.com/2021/02/18/phantom-types-in-swift/)

Python related:

4. [Flask Mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
5. [sqlalchemy-imageattach](https://sqlalchemy-imageattach.readthedocs.io/en/1.1.0/index.html)
6. [Celery task queue](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)

---

### Day 16: 24 March 2021

**Today**: Started learning about sqlalchemy-imageattach and alembic

**Thoughts:** I would have loved to have made more progress by now but got disctracted by new shiny objects.
Instead of just deleting the existing database and letting the ORM create the "updated" schema, I want to use a tool or something that can handle these changes to my models. Guess I got a bit spoiled by Django's tools.

However I did discover that the creators of SQLAlchemy created a tool called alembic.

**Key concepts:**
 
1. faasd stores the secrets at: /var/lib/faasd-provider/secrets and it is then binded to /var/openfaas/secrets for the function containers.
2. alembic can be used to manage database migrations of a SQLAlchemy database.
3. Swift: CRLF "\r\n" is treated as a single Unicode character. for c in string ... c == "\r\n"

**Links:**

1. [alembic](https://alembic.sqlalchemy.org/en/latest/)
2. [sqlalchemy-imageattach](https://sqlalchemy-imageattach.readthedocs.io/en/1.1.0/guide/declare.html)

---

### Day 17: 25 March 2021

**Today**: Alembic and SQLAlchemy-ImageAttach turned out be a bust for me at this time. Instead I have switched gears and will be just storing the file path in the database once the image has been downloaded.

**Thoughts:** n/a

**Key concepts:**

1. SQLAlchemy you can use .filter(Class.property.is_(None)) to check for NULLs.
2. You can also do the invert is_not().
3. To do an AND use and_ to combine expressions.

**Links:**

1. [Day 15,16 & 17 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-15-16-17/)
2. [Mako Templates for Python](https://www.makotemplates.org/)
3. [SO - Python Imports](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time)

---

### Day 18: 26 March 2021

**Today**: Today I managed to enable SSH on Home Assistant. I also managed to migrate my Home Assistant setup over to an external SSD via USB connected to the Raspberry Pi 3B.

**Thoughts:** I have been meaning to learn how to boot a Raspberry Pi of a SSD via USB for some time now and am glad I managed to do it today.

**Key concepts:**

1. SSH is disabled / non existent by default on Home Assitant OS. You need to install an add-on for it.
2. That weird ascii art you see during RSA key pair generation is called randomart.
3. -o VisualHostKey=yes to see randomart when you connect to SSH servers.
4. It is easy to make backups by taking snapshots of Home Assistant.
5. The snapshots live at /backup.
6. Raspberry Pi need you to enable USB host boot mode. I don't think you need this for Pi >= 4.
7. program_usb_boot_mode=1 -> config.txt to enable this.
8. To enable SSH on a fresh Pi SD install, create a file named ssh on the /boot portion.

**Links:**

1. [Day 18 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-18-setup-raspberry-pi-to-boot-of-a-ssd-via-usb-for-home-assistant/)
2. [Enable SSH in Home Assistant](https://andrejacobs.org/home-automation/home-automation-enable-ssh-on-home-assistant/)
3. [SSH randomart](https://superuser.com/questions/22535/what-is-randomart-produced-by-ssh-keygen)

---

### Day 19: 27 March 2021

**Today**: Learned how to install Redis on faasd and run a task queue using RQ.

**Thoughts:** I am quite chuffed that there was no hickups today in exploring new frameworks like RQ or running Redis on faasd.

**Key concepts:**

1. Redis is an in-memory data structure store, used as a database, cache, and message broker.
2. RQ can be used as a task queue system against Redis.
3. It is super easy to use!
4. Non existent tasks can be enqueued. Nothing will blow up (or work).
5. The worker will quit if it can't connect to Redis (or connection is lost).
6. Tasks can be enqueued even if there are no running workers at that time.

**Links:**

1. [Day 19 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-19-installing-redis-on-faasd-and-using-python-rq-as-a-task-queue/)
2. [Flask Mega Tutorial - Background Jobs](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs)
3. [Python RQ](https://python-rq.org/)
4. [Python Redis tutorial](https://realpython.com/python-redis/)

---

### Day 20: 28 March 2021

**Today**: Continued working on adding background task support to the Lego database learning project.

**Thoughts:** I have completed week 3 and not missed a single day of learning!

**Key concepts:**

1. Python: You can set an environment variable with
   os.environ['queue-name'] = 'johnny5'

2. Query...count is super slow on SQLAlchemy + MySQL/MariaDB.
3. Python variable args can be passed onto another function that takes variable args like this

		def perform(function, *args):
		    function(*args)

**Links:**

1. [Faster SQLAlchemy count](https://gist.github.com/hest/8798884)

---
