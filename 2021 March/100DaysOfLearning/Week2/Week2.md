# 100 Days Of Learning

## Log book - Week 2

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
