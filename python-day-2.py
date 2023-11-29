#list 

countries = ["Bangladesh", "India", "USA"]
countries[0]= "China"
print (countries)
print (countries[2])
print (countries[2][0])
print (countries[1:])
print (len(countries))
print (countries[-2])

print (type(countries))

mixup = [2, 1 , "Dhaka", True]

print (mixup)
print (type(mixup))
print (type(mixup[3]))

#list method

list1 = [1, 5, 6, 7]
list2 = ["banana", "apple", "mango", "orange"]
list3 = list2.copy()

print (list3)

#list1.extend(list2)
list2.append("lemon")
list1.insert(1, 100)
list2.remove ("banana")
#list2.clear()

list1.sort()
list1.reverse()

print (list1)
print (list2)

print (list1.index(5))
#-----------------------------------------------

my_list = [1, 2, 3, 4, 5]

# Remove and return the last item
popped_item = my_list.pop()

print("Popped Item:", popped_item)
print("Updated List:", my_list)

#----------------------------------------------

my_list2 = [1, 2, 3, 4, 5]

# Delete the item at index 2
del my_list2[2]

print("Updated List:", my_list2)

