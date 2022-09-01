numbers = [1,2,3,4,5]

# string_list = [str(num) for num in numbers]

# print(string_list)

# persons = ['Elie', 'Tim', 'Colt']

# answer = [persons[0] for persons in ['Elie', 'Tim', 'Colt']]
# val = [1,2,3,4,5,6]
# answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0 ]



# answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
# #the slice [::-1] is a quick way to reverse a string
# answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

# answer = [val for val in range(1,101) if val % 12 == 0] 

# print(answer)

# n = range(0,10)

# print(list(n))

nested = [[1,2,3], [4,5,6], [7,8,9]]

for l in nested:
    for val in l:
        print(val)