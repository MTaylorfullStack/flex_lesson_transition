## given a list, return the max, min, avg of the list


# declare a function, accept a list
    # declare var (max, min, sum)
    # loop through the arr
        # if arr value is greater than max
            # replace max
        # if arr value is less than min
            # replace min
        # add to sum
    # return max, min, avg

def max_min_avg(my_list):
    max=my_list[0]
    min=my_list[0]
    sum=0
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
        if my_list[i] < min:
            min = my_list[i]
        sum += my_list[i]
    print([max, min, sum/len(my_list)])
    return [max, min, sum/len(my_list)]

# print("this is test one")
max_min_avg([2,4,6,8,10])
# print("another test")
# max_min_avg([45,100,99,34,2])
