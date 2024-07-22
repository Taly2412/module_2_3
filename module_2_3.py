my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while my_list[a] >= 0 and a < len(my_list):
    b = my_list[a]
    a += 1
    if b > 0:
        print(b)
        continue