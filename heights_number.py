list1 = []

user_input = int(input("Enter Number of Items in List: "))

for i in range (user_input):
    item = int (input("Enter Items: "))
    list1.append(item)
    list1.sort ()

print ("Large Item: ",list1[-1])