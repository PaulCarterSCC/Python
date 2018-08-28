import numpy as np

numofservers =4
FiveMins=np.zeros(4*288*31).reshape(numofservers,31,288)
print(FiveMins[1,2,2])
FiveMins[1,2,2] =8
print(FiveMins[1,2,2])