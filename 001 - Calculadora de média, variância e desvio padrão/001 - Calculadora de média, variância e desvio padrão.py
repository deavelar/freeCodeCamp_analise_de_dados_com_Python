import numpy as np

def calculate(list):
  if len(list) != 9:
    print('List must contain nine numbers.')
  else:
    array = np.array(list)
    matriz = array.reshape(3,3)
    calculations = {
      'mean': [np.mean(matriz, axis=0), np.mean(matriz, axis=1), np.mean(matriz)],
      'variance' : [np.var(matriz, axis=0), np.var(matriz, axis=1), np.var(matriz)],
      'standard deviation' : [np.std(matriz, axis=0), np.std(matriz, axis=1), np.std(matriz)],
      'max' : [np.max(matriz, axis=0), np.max(matriz, axis=1), np.max(matriz)],
      'min' : [np.min(matriz, axis=0), np.min(matriz, axis=1), np.min(matriz)],
      'sum' : [np.sum(matriz, axis=0), np.sum(matriz, axis=1), np.sum(matriz)]
    }
    return calculations
  
print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))