import json
import numpy as np 

#m2 = "d p h u i e t q"
#m = '{"t": 66, "u": 72, "d": 90, "r": 84, "j": 36, "g": 50, "s": 94, "q": 62, "f": 35}'

jsonvalueinput = input()
laminasinput = input()
laminas = [laminasinput.split(" ")]
laminasout = []
jsonlaminas = json.loads(jsonvalueinput)
list_of_key = list(jsonlaminas.keys())
list_of_value = list(jsonlaminas.values())
suma = 0
a = ""
size = 1 
j = 0
i = 0
for dim in np.shape(laminas): size *= dim
c = 0

while c !=1:
      temp=0
      if laminas[0][j] == list_of_key[i]:
        a += list_of_key[i]
        suma += list_of_value[i]
        if j == size-1:
          j == size-1
          if laminas[0][j] == list_of_key[i]:
              c=1
        else:
            j = j+1
        i = 0
      elif list_of_key[i] == list_of_key[-1] and laminas[0][j] != laminas[0][-1]:
         i = 0
         j = j+1
      elif list_of_key[i] == list_of_key[-1] and laminas[0][j] == laminas[0][-1]:
        c = 1
      else:
          i = i+1
      
      
print(suma)
print(" ".join(a))

