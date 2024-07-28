# random choice and random shuffle 
import random

pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))
print(random.choice(pets))
print(random.choice(pets))
#we can use the random.choice instead of random.randInt(0,lent(somelist)-1) 
people = ['ferhat','mess3od','pedro','messi','van basten','kroos','zidane','foden']
print(people)
random.shuffle(people)
print(people)

#how to manually shuffle item without using the build it function random.shuffle
# we get the list
# we generate a random int for the number of shuffle we'll do
# we generate a random int in range 0 - len(list)-1 for the indexes of the shuffeled values
#  we hava a temp variable to store the shuffle between values 
people = ['ferhat','mess3od','pedro','messi','van basten','kroos','zidane','foden']
print(people)
for i in range(random.randint(0,len(people)-1)):
    str = random.randint(0,len(people)-1)
    to = random.randint(0,len(people)-1)
    temp = people[to]
    people[to] = people[str]
    people[str] = temp

print(people)