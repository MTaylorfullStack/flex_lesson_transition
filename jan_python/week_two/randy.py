import random
print(random.random()*30+20)


def randInt(min=0, max=100):
    num = random.random()*(max-min)+min
    return round(num)
print(randInt()) 		
print(randInt(max=50)) 
print(randInt(min=50)) 
print(randInt(min=50, max=500)) 