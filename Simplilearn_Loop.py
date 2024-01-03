s = "hello"

for i in s:
    print(i, end="")
print()


#find the avg of list of number

list1 = []

user_input = int(input("Enter Number of Items in List: "))

for n in range (user_input):
    item = int (input("Enter Items: "))
    list1.append(item)
print ("List:",list1)

sum = 0
for m in list1:
    print(m)
    sum = sum + m
print ("Avg:", sum/len(list1))

#table of a given number

table =9

for s in range(1,11):
    mul= s*table
    print(table, "*" ,s, "=", mul)




