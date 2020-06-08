#Leer laberinto
def mapa(archivo):
    return [x.split(" ") for x in open(archivo).readlines()]

#Buscar un parametro en el laberinto
def buscar_en_matriz(matriz, cont, para):
    if matriz == []:
        return (-1, -1)
    if para in matriz[0]:
        return (cont, matriz[0].index(para))
    return buscar_en_matriz(matriz[1:], cont + 1, para)

"""
Intento 3: Segregar los movimientos y controlarlos por una función master
"""
# Funcion por movimiento
def moverDerecha(y,x,matriz,movimientos):
  if (x+1) >= len(matriz[0]) or (x+1) < 0 or matriz[y][x+1] == '1' or matriz[y][x] == 'Y' or (buscar_en_matriz(matriz,0,'Y')[1] == x):
    mover(y,x,matriz,movimientos)
    pass
  else:  
    moverDerecha(y,x+1,matriz,movimientos+[[y,x]])

def moverArriba(y,x,matriz,movimientos):
  if (y-1) >= len(matriz) or (y-1) < 0 or matriz[y-1][x] == '1' or matriz[y][x] == 'Y' or (buscar_en_matriz(matriz,0,'Y')[0] == y):
    mover(y,x,matriz,movimientos)
    pass
  else:
    moverArriba(y-1,x,matriz,movimientos+[[y,x]])
    
def moverIzquierda(y,x,matriz,movimientos):
  if (x-1) >= len(matriz[0]) or (x-1) < 0 or matriz[y][x-1] == '1' or matriz[y][x] == 'Y' or (buscar_en_matriz(matriz,0,'Y')[1] == x):
    mover(y,x,matriz,movimientos)
    pass
  else:
    moverIzquierda(y,x-1,matriz,movimientos+[[y,x]])

def moverAbajo(y, x, matriz, movimientos):
  if (y+1) >= len(matriz) or (y+1) < 0 or matriz[y+1][x] == '1'or matriz[y][x] == 'Y' or (buscar_en_matriz(matriz,0,'Y')[0] == y):  
    mover(y,x,matriz,movimientos)
    pass
  else:
    moverAbajo(y+1, x, matriz, movimientos+[[y,x]])

## Funcion principal de movimiento
def mover(y,x,matriz,movimientos):
  if (y,x)== buscar_en_matriz(matriz,0,'Y'):
    movimientos = movimientos+[[y,x]]
    print(movimientos)
  elif x == buscar_en_matriz(matriz,0,'Y')[1] and (y < buscar_en_matriz(matriz,0,'Y')[0] and matriz[y+1][x] != '1'):
    #Abajo
    moverAbajo(y, x, matriz, movimientos)
  
  elif y == buscar_en_matriz(matriz,0,'Y')[0] and (x < buscar_en_matriz(matriz,0,'Y')[1] and matriz[y][x+1] != '1') :
    #Derecha
    moverDerecha(y, x, matriz, movimientos)

  elif x == buscar_en_matriz(matriz,0,'Y')[1] and (y > buscar_en_matriz(matriz,0,'Y')[0] and matriz[y-1][x] != '1'):
    #moverArriba
    moverArriba(y, x, matriz, movimientos)

  elif y == buscar_en_matriz(matriz,0,'Y')[0] and (x > buscar_en_matriz(matriz,0,'Y')[1] and matriz[y][x-1] != '1'):
    #Izquierda
    moverIzquierda(y, x, matriz, movimientos)

  elif matriz[y-1][x] == '1' and matriz[y+1][x] == '1' and matriz[y][x-1] == '1':
    moverDerecha(y,x,matriz,movimientos)

  elif matriz[y+1][x] == '1' and matriz[y][x+1] == '1' and matriz[y][x-1] == '1':
    moverArriba(y,x,matriz,movimientos)
  
  elif matriz[y+1][x] == '1' and matriz[y-1][x] == '1' and matriz[y][x+1] == '1':
    moverIzquierda(y,x,matriz,movimientos)
  
  elif matriz[y-1][x] == '1' and matriz[y][x+1] == '1' and matriz[y][x-1] == '1':
    moverAbajo(y,x,matriz,movimientos)



mover(buscar_en_matriz(mapa('matriz.txt'), 0, "X")[0],buscar_en_matriz(mapa('matriz.txt'), 0, "X")[1], mapa('matriz.txt'), [])