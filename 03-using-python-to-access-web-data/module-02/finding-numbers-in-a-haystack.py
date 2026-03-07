import re
file = open('regex_sum_2363260.txt')
line = file.read()
numbers = re.findall('[0-9]+', line)
intNumber = [int(i) for i in numbers]
total = sum(intNumber)
print('Total of all the numbers in file : ', total)