# Leer laberinto
def mapa(archivo):
  return [x.split(" ") for x in open(archivo).readlines()]

# Buscar un parametro en el laberinto
def buscar_en_matriz(matriz, cont, para):
  if matriz == []:
    return (-1, -1)
  if para in matriz[0]:
    return [cont, matriz[0].index(para)]
  return buscar_en_matriz(matriz[1:], cont + 1, para)

# Mover por el mapa
def mover(x, y, matriz, estado):
  # Encontro Y
  if [x,y] == buscar_en_matriz(matriz,0,'Y'):
    print ("Encontrado! %d,%d" % (x, y))
    return True
  # Hay una pared
  elif matriz[x][y] == '1':
    return False
  # Ya estuvo por aqui
  elif estado.__contains__([x,y]):
    return False

  print ('estoy en ' + str(x) + ' ' + str(y))

  if ((x < len(matriz) - 1 and mover(x + 1, y, matriz, estado + [[x, y]])) or (y > 0 and mover(x, y - 1, matriz, estado + [[x, y]])) or (x > 0 and mover(x - 1, y, matriz, estado + [[x, y]])) or (y < len(matriz[0]) - 1 and mover(x, y + 1, matriz, estado + [[x, y]]))):
    return True
  return False

def main(posicionX, matriz):
  if(mover(posicionX[0], posicionX[1], matriz, [])):
    print("¡Genial, terminamos!")
  else:
    print("Parece que el matriz no tiene solución :c")

main(buscar_en_matriz(mapa("matriz.txt"),0,'X'),mapa("matriz.txt"))