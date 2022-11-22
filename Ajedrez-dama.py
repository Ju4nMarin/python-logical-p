print ("------QUEEN------")

x1 = int(input("X1: "))
y1 = int(input("Y2: "))

x2 = int(input("X2: "))
y2 = int(input("Y2: "))

  
if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
  
  print ("YES")
  
else:
    
  print ("NO")