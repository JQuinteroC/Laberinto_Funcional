#Leer laberinto
def mapa(archivo):
  return [x.split(" ") for x in open(archivo).readlines()]

#Buscar un parametro en el laberinto
def buscar_en_matriz(matriz, cont, para):
    if matriz == []:
        return (-1,-1)
    if para in matriz[0]: 
        return (cont,matriz[0].index(para))
    return buscar_en_matriz(matriz[1:],cont+1)

def mover(Xy, Xx, Py, Px, matriz):
  if matriz[Py][Px] == '1':
    return (Xy, Xx)
  return (Py, Px)  
    
#print(len(mapa('matriz.txt')))
print(buscar_en_matriz(mapa('matriz.txt'),0))
