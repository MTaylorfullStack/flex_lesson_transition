def print_greeting(name="Vineet", num=1):
    if type(num) != int:
        return "Must pass an integer for num"
    for i in range(num):
        print(f"Hello {name}, welcome to session two Python!")
    return [num, name]

# print(print_greeting(num=[2324,2,3,3,4235234,345,25454,545], name="Cameron"))
# print_greeting("Vineet")
# print_greeting("Cameron")
# print_greeting("Andrew")
# print_greeting("Jason")
# print_greeting("Adam")
# print_greeting("Michael")

canvas=[
    [2,3,5,4,6],
    [6,7,4,7,9],
    [3,4,3,2,1],
    [8,8,6,3,1]
]

# print(canvas[1][4])

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

print(sports_directory['soccer'][1])

## loop through sports_directory and print out all of the basketball players and all of the soccer players

# for sport in sports_directory:
    # print(sport)
    # print(sports_directory[sport])
    # for i in range(len(sports_directory[sport])):
    #     print(sport, sports_directory[sport][i])
    # for name in sports_directory[sport]:
        # print(sport, name)


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

print(students[1]['last_name'])




