import memory_profiler as memory
import time
import random

names = ["jhon","corey","adam","steve","rick"]
subjects = ["maths","science","litrature","computer_science","arts"]

print("memory (before): {} Mb".format(memory.memory_usage()[0]))

def normal_function(nums_people):
    result = []
    for x in range(nums_people):
        person = {
            "id":x,
            "name":random.choice(names),
            "subject":random.choice(subjects)
        }
        result.append(person)
    return result

def gen_function(nums_people):
    for x in range(nums_people):
        person = {
            "id":x,
            "name": random.choice(names),
            "subject":random.choice(subjects)
        }
    yield person

number_of_peoples = 10000000
t1 = time.time()
people = gen_function(number_of_peoples)
t2 = time.time()

print("number of peoples :{}".format(number_of_peoples))

print("memory (after): {} Mb".format(memory.memory_usage()[0]))

print("time taken: {} seconds".format(t2-t1))