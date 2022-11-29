#COUNTDOWN: 5,4,3,2,1,0
def countdown(num):
    count = []
    for i in range(num, -1, -1):
        count.append(i)
    return count
print(countdown(5))



#PRINT_AND_RETURN [1,2]
def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([6,9]))

#FIRST PLUS LENGTH
list = [1,2,3,4,5]
def first_plus_length():
    sum = list[0] + len(list)
    print(sum)
first_plus_length()

#VALUES GREATER THAN SECOND
list = [1,2,3,4,5,6]
def greater_than_second():
    new_list = list[1:]
    print(new_list)
    print(len(new_list))
greater_than_second()

#THIS LENGTH THAT VALUE
def length_and_value(length, value):
    output = []
    for i in range(0, length):
        output.append(value)
    return output
print(length_and_value(6,12))
print(length_and_value(10,20))


