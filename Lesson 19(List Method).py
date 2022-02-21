number_list = [1, 2, 5, 7, 9, 1, 14]
number_list.append(20)
number_list.insert(4,4)
number_list.remove(2)
number_list.sort()
number_list.reverse()
number_list.pop()

print(number_list)
print(number_list.count(1))
print(number_list.index(9))

number_list_2 = number_list.copy()
number_list_2.clear()
print(number_list_2)
