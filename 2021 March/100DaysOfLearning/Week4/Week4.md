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
