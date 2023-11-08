list = [2, 3, 4, 5, 6, 7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        break

print(5%2)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
# #your code goes here
# for x in list:
#     sum = sum + x
# print(sum)

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

for l in range(10):
    if not l % 2 == 0:
        print(l+1)

list = [1, 2, 3]

for var in list:
    print(list)

def print_nums(x):
    for i in range(x):
        print(i)
    return
print_nums(10)