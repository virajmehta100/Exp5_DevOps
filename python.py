list1 = [1,34,32,12,1,34,90,90,32,21,1,2,2,3,4]
count = 0
n = len(list1)
for i in range(0,n):
    for j in range(i+1,n):
        if((list1[i]==list1[j])):
            count = count + 1
            print("Duplicate values are: ", list1[j])
print("Total duplicate values are: ", count)