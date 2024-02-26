my_list = []
for i in range(10):
    my_list.append(i)
    # print(my_list)

my_list.insert(2,"hello")
print(my_list)

# deleting element
del my_list[7]
my_list.remove("hello")
print(my_list)


a=my_list.pop(8)
print(f"popped element is {a}")
print("returning new list after")
print(my_list)
print("count:")
print(my_list.count(9))


print(my_list.reverse())