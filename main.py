from archivo import Archivo

# Abrir y mostrar el archivo con sus números de línea
nombre = input('Nombre del archivo:')
archivo = Archivo(nombre)

archivo.muestra()

# Imprimir estadísticas del archivo
print('Vocales:', archivo.cuentaVocales())
print('Consonantes:', archivo.cuentaConsonantes())
print('Signos de puntuación:', archivo.cuentaPuntuacion())
print('Espacios:', archivo.cuentaEspacios())
print('Palabras:', archivo.cuentaPalabras())
print('Líneas:', archivo.cuentaLineas())
print('Mayúsculas:', archivo.cuentaMayusculas())
print('Minúsculas:', archivo.cuentaMinusculas())

# Copiar el archivo
destino = input('Nombre de la copia: ')
archivo.copiar(destino)

# Cargar la copia y mostrarla 
copia = Archivo(destino)
print('Contenido de la copia:')
copia.muestra()

# Muestra el contenido de todo el archivo en hexadecimal
archivo.convertirHexadecimal()

# Muestra todo el contenido del archivo en minúsculas
archivo.convertirMinusculas()

# Muestra todo el contenido del archivo en mayúsculas
archivo.convertirMayusculas()
