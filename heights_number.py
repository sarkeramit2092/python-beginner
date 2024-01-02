list1 = []

user_input = int(input("Enter Number of Items in List: "))

for i in range (user_input):
    item = int (input("Enter Items: "))
    list1.append(item)
print ("List:",list1)

heights_num = list1[0]
#print ("Heights_number: ",heights_num)
for item in list1:
        if item > heights_num:
            heights_num = item
print ("Heights Number---: ",heights_num)