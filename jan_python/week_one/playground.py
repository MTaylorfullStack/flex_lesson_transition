print("Hello World")

## Data Types

## String
collection_of_characters="hrwajfaiugh5uq34ht834tgu89398ht4gh0q4tn"

collection_of_characters+="!!!!!!!!!!!!!"

name="Adam"
stack="Python"

# print(f"The student {name} is in the {stack} stack")

## Numbers
## Operators: +, -, /, *, %

ten=10
one_hundred=100

# print(one_hundred-ten)

## Lists

students = ['Vineet', 'Adam', 'Cameron', 'Roxanne']

# print(students[2])
# print(students.length)
# help(list)

# students.pop()
# print(students)
# students.append("Roxanne")
# print(students)

## Dictionaries


player = {'first_name':  'Michael', 'last_name' : 'Jordan'}


# print(students[0]['first_name'])

## Conditionals and Loops

# if(bird['feathers']=='blue'){
#     console.log("it is a blue bird")
# }

# if bird['feathers']=='blue':
#     print("it is a blue bird")
# elif bird['feathers']=='red':
#     print("It is a red bird")
# else:
#     print("it is not a red or a blue bird")

## Loops

my_list=[1,2,3,4,5,6,7,8]

for i in range(len(my_list)):
    print(my_list[i])

bird={
    'feathers':"blue",
    'wings':'2',
    'name':"floppy",
    'friends':["Tom", "Tweety", "Woodie"]
}

for thing in bird:
    print(thing, bird[thing])