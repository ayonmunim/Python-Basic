number_list = [1, 2, 1, 5, 6, 7, 5, 10]
unique = []

for number in number_list:
    if number not in unique:
        unique.append(number)
print(unique)

#Ex:2

num = [22,22,24,25]
un = []
for number in num:
    if number not in un:
        un.append(number)
print(un)