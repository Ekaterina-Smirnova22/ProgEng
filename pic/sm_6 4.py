def cort(incoming_list, num):
    if num not in incoming_list:
        return 0
    if incoming_list.count(num) == 1:
        return incoming_list [incoming_list.index(num):]
    return incoming_list[incoming_list.index(num):incoming_list.index(num, incoming_list.index(num)+1) +1 ]

print(cort((1, 2, 3), 8))
print(cort((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(cort((1, 2, 8, 5, 1, 2, 9), 8))
