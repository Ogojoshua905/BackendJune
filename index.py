names = ["miracle", "kayode", "clara", "robert"]
serial_num = [254,456,782,991]

for x,y in zip(names, serial_num):
    print(x,y)
# for name in names:
#     print(name)

# for index, name in enumerate(names):
#     print((index, name))


# num = 0

#length_of_list = len(names)

# while num < length_of_list:
#     print(names[num])
#     num+=1 #or num + 1

# for num in range(10):
#     print(num)
persons = ["miracle", "kayode", "clara", "robert"]

emails = [f"{person}@gmail.com" for person in persons if person !="miracle"]

print(emails)