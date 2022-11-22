array = [4 , 0 , 5 , 0 , 3 , 0 , 0 , 5]

for i in range(0,7):
 if array[i] == 0:
    array.pop(i)
    array.append(0)
    if array[i] == 0:
      array.pop(i)
      array.append(0)
print (array)
