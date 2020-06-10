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
Intento 4: Metodo del ciego, pegarse a una pared
"""
# Funcion por movimiento
def moverDerecha(y,x,matriz,movimientos):
  if (x+1) >= len(matriz[0]) or (x+1) < 0 or matriz[y][x+1] == '1' or matriz[y][x] == 'Y':
    moverCiego(y,x,matriz,movimientos, y,x-1)
    pass
  else:  
    moverDerecha(y,x+1,matriz,movimientos+[[y,x]])

def moverArriba(y,x,matriz,movimientos):
  if (y-1) >= len(matriz) or (y-1) < 0 or matriz[y-1][x] == '1' or matriz[y][x] == 'Y':
    moverCiego(y,x,matriz,movimientos, y+1,x)
    pass
  else:
    moverArriba(y-1,x,matriz,movimientos+[[y,x]])

def moverIzquierda(y,x,matriz,movimientos ):
  if (x-1) >= len(matriz[0]) or (x-1) < 0 or matriz[y][x-1] == '1' or matriz[y][x] == 'Y':
    moverCiego(y,x,matriz,movimientos, y, x+1)
    pass
  else:
    moverIzquierda(y,x-1,matriz,movimientos+[[y,x]])

def moverAbajo(y, x, matriz, movimientos):
  if (y+1) >= len(matriz) or (y+1) < 0 or matriz[y+1][x] == '1'or matriz[y][x] == 'Y':  
    moverCiego(y,x,matriz,movimientos, y-1,x)
    pass
  else:
    moverAbajo(y+1, x, matriz, movimientos+[[y,x]])

def atrapado(y,x,matriz,movimientos,y1, x1):
  if x > x1:
    moverIzquierda(y, x, matriz, movimientos)
  elif x < x1:
    moverDerecha(y, x, matriz, movimientos)
  elif y > y1:
    moverArriba(y, x, matriz, movimientos)
  else:
    moverAbajo(y, x, matriz, movimientos)

def imprimir(movimientos,  k):
  if k == []:
    print(movimientos)
    pass
  elif k[0] == movimientos[0]:
    print(movimientos[movimientos.index(k[0],1):])
    pass
  else:
    imprimir(movimientos, k[1:])
  pass

def moverCiego(y,x,matriz,movimientos,y1, x1):
  if (y,x) == buscar_en_matriz(matriz,0,'Y'):
    movimientos = movimientos+[[y,x]]
    imprimir(movimientos, movimientos[1:])
  elif matriz[y+1][x] == '1':
    if (matriz[y][x+1] == '0' or matriz[y][x+1] == 'Y') and x+1 != x1:
      moverDerecha(y,x,matriz,movimientos)
    elif (matriz[y-1][x] == '0' or matriz[y-1][x] == 'Y') and y-1 != y1:
      moverArriba(y,x,matriz,movimientos)
    elif (matriz[y][x-1] == '0' or matriz[y][x-1] == 'Y') and x-1 != x1:
      moverIzquierda(y,x,matriz,movimientos)
    else:
      atrapado(y,x,matriz,movimientos,y1,x1)
      
  elif matriz[y][x+1] == '1':
    if (matriz[y-1][x] == '0' or matriz[y-1][x] == 'Y') and y-1 != y1:
      moverArriba(y,x,matriz,movimientos)
    elif (matriz[y][x-1] == '0' or matriz[y][x-1] == 'Y') and x-1 != x1:
      moverIzquierda(y,x,matriz,movimientos)
    elif (matriz[y+1][x] == '0' or matriz[y+1][x] == 'Y') and y+1 != y1:
      moverAbajo(y,x,matriz,movimientos)
    else:
      atrapado(y,x,matriz,movimientos,y1,x1)

  elif matriz[y-1][x] == '1':
    if (matriz[y][x-1] == '0' or matriz[y][x-1] == 'Y') and x-1 != x1:
      moverIzquierda(y,x,matriz,movimientos)
    elif (matriz[y+1][x] == '0' or matriz[y+1][x] == 'Y') and y+1 != y1:
      moverAbajo(y,x,matriz,movimientos)
    elif (matriz[y][x+1] == '0' or matriz[y][x+1] == 'Y') and x+1 != x1:
      moverDerecha(y,x,matriz,movimientos)
    else:
      atrapado(y,x,matriz,movimientos,y1,x1)
    
  elif matriz[y][x-1] == '1':
    if (matriz[y+1][x] == '0' or matriz[y+1][x] == 'Y') and y+1 != y1:
      moverAbajo(y,x,matriz,movimientos)
    elif (matriz[y][x+1] == '0' or matriz[y][x+1] == 'Y') and x+1 != x1:
      moverDerecha(y,x,matriz,movimientos)
    elif (matriz[y-1][x] == '0' or matriz[y-1][x] == 'Y') and y-1 != y1:
      moverArriba(y,x,matriz,movimientos)
    else:
      atrapado(y,x,matriz,movimientos,y1,x1)
    
  else:
    if matriz[y+1][x] == '0' or matriz[y+1][x] == 'Y':
      moverAbajo(y,x,matriz,movimientos)
    elif matriz[y][x+1] == '0' or matriz[y][x+1] == 'Y':
      moverDerecha(y,x,matriz,movimientos)
    elif matriz[y-1][x] == '0' or matriz[y-1][x] == 'Y':
      moverArriba(y,x,matriz,movimientos)
    elif matriz[y][x-1] == '0' or matriz[y][x-1] == 'Y':
      moverIzquierda(y,x,matriz,movimientos)

moverCiego(buscar_en_matriz(mapa('matriz.txt'), 0, "X")[0],buscar_en_matriz(mapa('matriz.txt'), 0, "X")[1], mapa('matriz.txt'), [],-1,-1)