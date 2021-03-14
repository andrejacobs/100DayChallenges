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
