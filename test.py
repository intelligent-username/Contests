list_a = [1, 2, 3]
list_b = [4, 5, 6]

while list_a != list_b:
    
    print("Lists are not equal yet")
    print("List a:", list_a)
    print("List b:", list_b)
    
    list_a[0] += 1
    list_a[1] += 1
    list_a[2] += 1

print("----\nLists are now equal.\n----")
print("List a:", list_a)
print("List b:", list_b)
