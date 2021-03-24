# 100 Days Of Learning

This is my first challenge to kickstart the "100 Days of X" habbit and I chose a generic category of Learning as to not restrict myself to a single topic just yet.

The main goal is to oil the machine, fire it up and keep it running.

**What do I want to learn (more of / not master) during this challenge?**

* [AWS](https://aws.amazon.com/)
* Serverless technologies. Starting with [Serverless for everyone else](https://gumroad.com/l/serverless-for-everyone-else)
* Modern iOS technologies like SwiftUI and Combine

## Rules

1. Learn about a topic for minimum an hour a day.
2. Take notes and update this log.
3. Tweet daily progress with the hashtag: #100DaysOfLearning

The challenge would be a failure if I have gone 3 consecutive days without following the rules.

## Log book

### Day 0: 8 March 2021

**Today**: Started going through Alex Ellis's book "Serverless for everyone else" and learned about OpenFaaS, faasd and multipass.

**Thoughts:** I actually liked learning about setting up faasd locally on my Mac and deploying my first FaaS (cowsay / ASCII Cows)

**Key concepts:**

1. Kubernetes (a.k.a K8s): Orchestrates container deployment, scaling, and management.
2. FaaS: Function as a Service.
2. OpenFaaS: Makes it simple to deploy both functions and existing code to Kubernetes.
3. faasd: Light-weight way of running OpenFaaS. Not really scalable but still very cool.
4. faasd swaps out Kubernetes for containerd which is a low level container runtime.
5. Multipass: Amazing! How did I not know about this. Super easy way to run Ubuntu instances.

**Links:**

1. [Day 0 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-0-serverless-openfaas-and-multipass/)
2. [Serverless for Everyone Else](https://gumroad.com/l/serverless-for-everyone-else)
3. [Alex Ellis' blog](https://blog.alexellis.io/)
4. [OpenFaaS](https://www.openfaas.com/)
5. [faasd](https://github.com/openfaas/faasd)
6. [Kubernetes](https://kubernetes.io/)
7. [Multipass](https://multipass.run/)

---

### Day 1: 9 March 2021

**Today**: Signed up to Notion and learned the basics of using Notion. Also managed to setup faas-cli on my Mac and invoke a function.

**Thoughts:** Notion has been on my radar for a while but at face value it looked complicated. I am so glad I took the plunge! This is THE tool I have been looking for. In fact I managed to write the entire blog post in it and export it to markdown and then add to wordpress.

**Key concepts:**

1. Notion is awesome. Just try it!
2. faas-cli can be installed on Mac using brew (I love brew!)
3. faas-cli is pretty easy to setup and start using against faasd

**Links:**

1. [Day 1 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-1-notion-and-faas-cli/)
2. [faas-cli](https://github.com/openfaas/faas-cli)
3. [Notion](https://www.notion.so/)

---

### Day 2: 10 March 2021

**Today**: Managed to deploy my first function using faasd and faas-cli. Was only the blank python3 template but still stoked!

**Thoughts:** The learning challenge is going well so far and I have a bit of momentum at the moment. I won't lie, having a 3.5, 1.5 year old and a very demanding full time job and then to still try and learn new things (and not just veg out on the sofa) is no easy task. I get my energy from knowing that there is actually people on Twitter following my progress and liking my journey. Thank you to every one!

**Key concepts:**

1. OpenFaaS gateway can be accessed as a REST API (JSON)
2. jq is handy cli for working with JSON
3. OpenFaaS functions are packaged as Docker container images
4. GitHub has a container registry as well, Nice! https://github.com/features/packages
5. OpenFaaS has templates for various languages and stacks to help bootstrap a new function
6. To get the list of templates: faas-cli template store list

**Links:**

1. [Day 2 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-2-deploying-my-first-python-based-function/)
2. [Serverless for Everyone Else](https://gumroad.com/l/serverless-for-everyone-else)

---

### Day 3: 11 March 2021

**Today**: Did some more learning about OpenFaaS and how to call another API end point. Also refreshed a bit on Swift knowledge.

**Thoughts:** It is good to get out of your comfort zone a bit.

**Key concepts:**

1. You can invoke your faasd function directly by calling the API end point.
2. If you are using the node template, then you must install npm packages in the same directory where the handler.js file is.
3. Swift's value types like String, Array, Dictionary etc. uses Copy-on-Write.

**Links:**

1. [Day 3 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-3-calling-another-api-from-our-openfaas-function/)

---

### Day 4: 12 March 2021

**Today**: Using Environment variables and Secrets in OpenFaaS. Also some more Swift refreshments.

**Thoughts:** Managed to do 5 days straight of learning and writing, so I am quite chuffed.

**Key concepts:**

1. You can configure environment variables in the yaml file and then your function can access it as per norm.
2. YAML does not like tabs!
3. You can also supply secrets to your function and these are made available to the function at the path: /var/openfaas/secrets/NAME_OF_SECRET.
4. A secret name must start and end with an alphanumeric character and can only contain lower-case alphanumeric characters, '-' or '.'
5. Swift: Mutating a Struct (value type) instance is not the same as mutating an Object (reference) instance.
6. Swift: Members need to be declared as var in order to be mutable, however the variable declaration still determines if that member is allowed to be mutated or not.

**Links:**

1. [Day 4 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-4-using-environment-variables-and-secrets-in-openfaas/)

---

### Day 5: 13 March 2021

**Today**: Managed to call an OpenFaaS function asynchronously and deliver the results to another function which ends up emailing to myself.

**Thoughts:** It was a lot harder than I thought to try and send an email from the container etc.

**Key concepts:**

1. docker-compose.yaml can be modified to change the listening port of the gateway.
2. To restart faasd: sudo systemctl daemon-reload && sudo systemctl restart faasd.
3. Each end point have an /async-function/ equivalent.
4. You can not send a GET request to these end points but instead need to POST to them.
5. By default the async promise response go to /dev/null.
6. You need to use a callback end point to receive the promise's response.
7. To check the log for a function: sudo journalctl -t openfaas-fn:FUNCTION_NAME

**Links:**

1. [Day 5 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-5-invoking-an-openfaas-function-asynchronously/)
2. [OpenFaaS async](https://docs.openfaas.com/reference/async/)

---

### Day 6: 14 March 2021

**Today**: Setup a MariaDB database in AWS RDS and connected to it using MySQLWorkbench. This is the first part of a small little project that will make use of different concepts to learn and explore.

**Thoughts:** Week 1 has been completed! Even if I only had 3 hours sleep last night. Kids man! Regardless it has been an amazing week of learning.

**Key concepts:**

n/a today.

**Links:**

1. [Day 6 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-6-lets-build-our-own-lego-database-using-mariadb-in-aws-rds-and-openfaas/)
2. [Amazon Web Services](https://aws.amazon.com/)

---

### Day 7: 15 March 2021

**Today**: Setup Python on macOS using pyenv to manage Python versions and using virtual environments to manage dependencies.

**Thoughts:** Start of week 2.

**Key concepts:**

n/a today.

**Links:**

1. [Day 7 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-7-setting-up-python-using-pyenv-and-virtual-environments/)
2. [Table Saw Safety](https://www.youtube.com/watch?v=eUx8oTIALmg)

---

### Day 8: 16 March 2021

**Today**: Swift: learned about the supplied function "dump" and #file and #line. Dived more into how I could use Flask and OpenFaaS for my legodb learning project.

**Thoughts:** Did not make as much progress tonight as I would have hoped. But this is understandable because not everything is just going to click in place first time, especially since I am not just following a recipe but rather trying to learn how I can accomplish a certain project.

**Key concepts:**

1. Swift: I find the "if case let .someEnum(bindVar) = some.optional" syntax hard to remember.
2. Swift has a "built-in" dump function.
3. You can write a function like "func someFunc(StaticString file = #file, Int line = #line)" and thus get passed the file and line of the calling code.
4. OpenFaaS has a template for python3-flask and this is barebones. The python3-http one gives you a lot more control and is still flask based.
5. OpenFaaS has a template for a barebones "supply your own stuff" with a minimal Dockerfile.

**Links:**

1. [Build a Flask microservice with OpenFaaS](https://www.openfaas.com/blog/openfaas-flask/)
2. [OpenFaaS Flask template](https://github.com/openfaas/python-flask-template)
3. [Alpha Binaural Beats](https://www.youtube.com/watch?v=p2_zDvtPQ-g)

---

### Day 9: 17 March 2021

**Today**: Explored a bit more of how the faas-cli templates work. Got a bare bones mocked API for my legodb project.

**Thoughts:** Stay focussed on the goal and not get distracted.

**Key concepts:**

1. The templates is instrumental during the faas-cli build step.
2. The non-core templates must be pulled to your local dir first: faas-cli template store pull python3-flask.
3. faas-cli up is a combination of build, push and deploy.
4. Functions can be removed with: faas-cli remove FUNCTION_NAME.
5. Be careful of programmer traps. Especially when the goal is to learn and not build new shinies.

**Links:**

1. [Day 8 & 9 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-8-9-first-pass-of-the-lego-database-api/)
2. [Free: New Serverless on Kubernetes Course by the LinuxFoundation](https://www.openfaas.com/blog/introduction-to-serverless-linuxfoundation/)
3. [Building a TODO API in Golang with Kubernetes](https://levelup.gitconnected.com/building-a-todo-api-in-golang-with-kubernetes-1ec593f85029)

---

### Day 10: 18 March 2021

**Today**: Managed to install mariadb connector and dependencies locally as well as being able to connect to the Amazon RDS instance.

**Thoughts:** Tried to get the mariadb-connector-c to install during faas-cli up but it doesn't look like it is being picked up by the pip install mariadb during the docker build.

**Key concepts:**

1. There is now a mariadb connector for Python (You had to use the MySQL one before).
2. The Python package requires the mariadb-connector-c library.
3. The Dockerfile from the python3-http template has the following ARG ADDITIONAL_PACKAGE.
4. Which means that from your yaml file you can supply extra pacakges to be installed:

		build_args:
	      ADDITIONAL_PACKAGE: mariadb-connector-c

**Links:**

n/a

---

### Day 11: 19 March 2021

**Today**: Continued adding MariaDB support to my OpenFaaS function. Learned about Swift 5's string interpolation.

**Thoughts:** It is nice that there is an OpenFaaS Slack channel and you can get help when you get stuck.

**Key concepts:**

1. The template.yml contains a section build_options that can be used to install system packages (sort of like apt).
2. Use "faas-cli up --build-option dev" to install the extra packages like mariadb-connector-c.
3. Swift 5: ExpressibleByStringLiteral & ExpressibleByStringInterpolation allow you to add your own custom string interpolation.

**Links:**

1. [Day 10 & 11 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-10-11-connecting-to-mariadb-from-python-and-openfaas/)
2. [OpenFaaS build_options](https://docs.openfaas.com/cli/build/)
3. [OpenFaaS community](https://docs.openfaas.com/community/)
4. [Programming Idioms](https://programming-idioms.org/)

---

### Day 12: 20 March 2021

**Today**: Learned about using SQLAlchemy as an ORM. Managed to get all the Lego sets and create new ones.

**Thoughts:** Today felt like a win.

**Key concepts:**

1. Use faas-cli logs, you can also --tail
2. SQLAlchemy: create_engine("mariadb+mariadbconnector://user:pass@some_mariadb:port/dbname?charset=utf8mb4")
3. Relative (.) Python import: from .models import LegoSet
4. To get the generated ID:

		session.add(legoset)
		session.commit()
		session.refresh(legoset)
		newID = legoset.id
		
**Links:**

1. [Day 12 blog post](https://andrejacobs.org/100-days-challenge/100-days-of-learning-day-12-using-sqlalchemy-as-an-orm-for-our-lego-database/)
2. [SQLAlchemy tutorial](https://www.pythoncentral.io/overview-sqlalchemys-expression-language-orm-queries/)
3. [OpenFaaS example of relative import](https://www.openfaas.com/blog/multifile-python-functions/)

---

### Day 13: 21 March 2021

**Today**: I want to add code syntax highlighting to my blog so I learned about highlight.js. Also I am having to dust off how I run WordPress locally for theme / plugin development.

**Thoughts:** I have now done 14 days of Learning. I am feeling pretty good about it.

My Docker setup I use for running local WordPress (which I have not touched since 2019) no longer works as expected.
So I diving deep in resetting all this up. To make matter worst is I have run into issues with gulp, npm and dependencies. Haha this is probably more of a reason to run more things in Docker containers.

**Key concepts:**

1. The Markdown I export from Notion and then import into WordPress specifies code blocks using \<pre>\<code class="language-python"> style tags.
2. Highlight.js can pickup this at rendering time and apply syntax highlighting.
3. Docker Volumes is the correct approach for storing data in a way that it can be restored when spinning up containers.

**Links:**

1. [highlight.js](https://highlightjs.org/)
2. [Docker Volumes](https://docs.docker.com/storage/volumes/)
3. [Official Docker compose and WordPress](https://docs.docker.com/compose/wordpress/)

---

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
