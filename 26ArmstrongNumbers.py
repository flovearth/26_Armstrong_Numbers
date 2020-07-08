given_number = input('Please enter a number: ')
given_number_set = set(given_number)
given_number_list = list(given_number)
numeric_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
union_set = given_number_set.union(numeric_set)
n = len(given_number)

if len(union_set) > len(numeric_set):
    print('It is an invalid entry. Don\'t use non-numeric, float, or negative values!')
else:
    result = 0
    for i in given_number_list:
        result += int(i) ** n

    if str(result) == given_number:
        print('This is Armstrong number.')
    else:
        print('This is not an Armstrong number.')
