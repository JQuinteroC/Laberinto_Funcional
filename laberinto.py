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
Intento 2: mover derecha-izquierda o arriba-abajo
"""
"""
#Funcion para moverse a la derecha
def moverDer(y, x, matriz, movimientos, aux):
  print(movimientos)
  if ((x+aux) >= len(matriz[0]) or (x+aux) < 0):
    pass
  if matriz[y][x] == '1' or (matriz[y-1][x-aux] != '1' or matriz[y+1][x-aux] != '1'):
    
  #  print("pared horizontal") 
  #  if(matriz[y][x-aux] != 'Y'):
  #    moverVer(y,x-aux,matriz,movimientos, 0)
  #  print(movimientos)
  
    pass
  elif matriz[y][x+1] != '1':
    moverDer(y,x+1,matriz,movimientos+[[y,x]], 1)
  elif matriz[y][x-1] != '1':  
    moverDer(y,x-1,matriz,movimientos+[[y,x]], -1)

def moverVer(y, x, matriz, movimientos, aux):
  print(movimientos)
  print(str(x)+' '+ str(y))
  if ((y+aux) >= len(matriz) or (y+aux) < 0):
    pass
  if matriz[y][x] == '1'or (matriz[y-aux][x-1] != '1' or matriz[y-aux][x+1] != '1'):
    print("pared Vertical")
    if(matriz[y][x] != 'Y'):
      moverDer(y,x,matriz,movimientos, 0)
    print(movimientos)
    pass
  elif matriz[y-1][x] != '1':  
    moverVer(y-1,x,matriz,movimientos+[[y,x]], -1)
  elif matriz[y+1][x] != '1':
    moverVer(y+1,x,matriz,movimientos+[[y,x]], 1)
"""

"""
Intento 3: Segregar los movimientos y controlarlos por una función master
"""
# Funcion por movimiento
def moverDerecha(y,x,matriz,movimientos):
  print(movimientos)
  if (x+1) >= len(matriz[0]) or (x+1) < 0:
    pass
  else:  
    moverDerecha(y,x+1,matriz,movimientos+[[y,x]])

def moverArriba(y,x,matriz,movimientos):
  print(movimientos)
  if (y-1) >= len(matriz) or (y-1) < 0:
    pass
  else:
    moverArriba(y-1,x,matriz,movimientos+[[y,x]])
    
def moverIzquieda(y,x,matriz,movimientos):
  print(movimientos)
  if (x-1) >= len(matriz[0]) or (x-1) < 0:
    pass
  else:
    moverIzquieda(y,x-1,matriz,movimientos)

def moverAbajo(y, x, matriz, movimientos):
  print(movimientos)
  if (y+1) >= len(matriz) or (y+1) < 0:
    pass
  else:
    moverAbajo(y+1, x, matriz, movimientos)

## Funcion principal de movimiento
def mover(y,x,matriz,movimientos):
  if(buscar_en_matriz(matriz,0,'X')[1] == buscar_en_matriz(matriz,0,'Y')[1] and buscar_en_matriz(matriz,0,'X')[0] < buscar_en_matriz(matriz,0,'Y')[0] ):
  #Abajo
    pass  
  elif(buscar_en_matriz(matriz,0,'X')[1] == buscar_en_matriz(matriz,0,'Y')[1] and buscar_en_matriz(matriz,0,'X')[0] > buscar_en_matriz(matriz,0,'Y')[0]):
  #moverArriba
    pass
  elif(buscar_en_matriz(matriz,0,'X')[0] == buscar_en_matriz(matriz,0,'Y')[0] and buscar_en_matriz(matriz,0,'X')[1] > buscar_en_matriz(matriz,0,'Y')[1]):
  #Izquierda
    pass
  elif(buscar_en_matriz(matriz,0,'X')[0] == buscar_en_matriz(matriz,0,'Y')[0] and buscar_en_matriz(matriz,0,'X')[1] < buscar_en_matriz(matriz,0,'Y')[1]):
  #Derecha
    pass
  elif(buscar_en_matriz(matriz,0,'X')[0] > buscar_en_matriz(matriz,0,'Y')[0] and buscar_en_matriz(matriz,0,'X')[1] < buscar_en_matriz(matriz,0,'Y')[1]):
  #Derecha arriba
    pass
  elif(buscar_en_matriz(matriz,0,'X')[0] < buscar_en_matriz(matriz,0,'Y')[0] and buscar_en_matriz(matriz,0,'X')[1] < buscar_en_matriz(matriz,0,'Y')[1]):
  #Derecha abajo   
    pass
  elif(buscar_en_matriz(matriz,0,'X')[0] > buscar_en_matriz(matriz,0,'Y')[0] and buscar_en_matriz(matriz,0,'X')[1] > buscar_en_matriz(matriz,0,'Y')[1]):
  #Izquierda arriba
    pass
  elif(buscar_en_matriz(matriz,0,'X')[0] < buscar_en_matriz(matriz,0,'Y')[0] and buscar_en_matriz(matriz,0,'X')[1] > buscar_en_matriz(matriz,0,'Y')[1]):
  #Izquierda abajo   
    pass

"""
11 1 1 1 1 1 1 1 1 1 1
21 0 1 0 0 0 0 x X 1 1
31 0 1 1 1 1 1 x 1 x 1
41 0 0 0 0 0 0 x 0 1 1
51 0 1 1 1 1 1 1 1 1 1
61 y 0 0 0 0 0 0 0 Y 1
71 1 1 1 1 1 1 1 1 1 1
"""

#print(buscar_en_matriz(mapa('matriz.txt'), 0, "X")[0])
#moverDer(buscar_en_matriz(mapa('matriz.txt'), 0, "X")[0], buscar_en_matriz(mapa('matriz.txt'), 0, "X")[1], mapa('matriz.txt'), [], 0)
