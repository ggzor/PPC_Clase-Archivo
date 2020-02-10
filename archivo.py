# Importar la función exit
from sys import exit

# Definición de la clase Archivo
class Archivo:
    def __init__(self, nombre):
        """Constructor de la clase Archivo, requiere un nombre
           de archivo existente para poder ser instanciada"""

        try:
            # Intentar abrir el archivo
            self.f = open(nombre, 'r')
            self.nombre = nombre
        except:
            # Si no se puede abrir el archivo, entonces se termina el programa
            print('No se puede abrir el archivo', nombre)
            exit()

    def muestra(self):
        """Muestra el archivo línea por línea, con su número
           de línea correspondiente"""

        # Mostrar línea por línea
        i = 1
        for linea in self.f:
            print(f'{i:3} {linea}', end='')
            i += 1
        
        # Regresar el apuntador del archivo al inicio
        self.f.seek(0)

    def cuentaSi(self, condicion):
        """Cuenta cuántos de los caracteres en el archivo cumplen con la condición dada. 
           Realiza una conversión a minúsculas antes de verificar la condición."""

        # Función interna para contar los caracteres que están en 
        # el conjunto en una línea
        def contar(s):
            contador = 0

            # Verificación de cada caracter de la cadena
            for i in range(len(s)):
                if condicion(s[i].lower()):
                    contador += 1

            return contador

        # Realizar el conteo en todo el archivo
        contador = 0
        for linea in self.f:
            contador += contar(linea)

        # Devolver el apuntador del archivo al inicio
        self.f.seek(0)

        return contador

    def cuentaVocales(self):
        """Cuenta cuántas vocales hay en el archivo"""
        return self.cuentaSi(lambda c: c in set('aeiouáéíóú'))

    def cuentaConsonantes(self):
        """Cuenta cuántas consonantes hay en el archivo"""
        return self.cuentaSi(lambda c: c in set('bcdfghjklmnpqrstvwxyz'))

    def cuentaPuntuacion(self):
        """Cuenta cuántos signos de puntuación hay en el archivo"""
        return self.cuentaSi(lambda c: c in set('¿?¡!"\',.:;-_'))

    def cuentaEspacios(self):
        """Cuenta cuántos espacios hay en el archivo, incluyendo tabulaciones."""
        return self.cuentaSi(lambda c: c in set(' \t'))

    def cuentaMayusculas(self):
        """Cuenta cuántas letras mayúsculas hay en el archivo."""
        return self.cuentaSi(str.isupper)
    
    def cuentaMinúsculas(self):
        """Cuenta cuántas letras minúsculas hay en el archivo."""
        return self.cuentaSi(str.islower)

    def cuentaPalabras(self):
        """Cuenta cuántas palabras hay en el archivo"""
        contador = 0

        # Por cada línea
        for linea in self.f:
            # Inicialmente no se está dentro de una palabra
            dentroPalabra = False

            # Por cada caracter de la línea
            for c in linea:
                # Si encontramos una letra y no estamos dentro de una palabra
                # Entonces ahora sí estamos en una palabra y es una nueva palabra
                if c.isletter() and not dentroPalabra:
                    dentroPalabra = True
                    contador += 1

                # Si encontramos algo que no es una letra y estabamos en una palabra
                # Entonces ya terminó la palabra
                if not c.isletter() and dentroPalabra:
                    dentroPalabra = False

        # Devolver el apuntador del archivo al inicio
        self.f.seek(0)

        return contador

    def cuentaLineas(self):
        """Cuenta cuántas líneas tiene el archivo"""
        contador = 0

        # Incrementar el contador de archivo por cada línea
        for _ in self.f:
            contador += 1

        # Devolver el apuntador del archivo al inicio
        self.f.seek(0)

        return contador

    def copiar(self, destino):
        """Copia el archivo actual al archivo con el nombre especificado"""
        # Abrir el archivo y copiar linea por linea
        with open(destino, 'w') as destino:
            for l in self.f:
                # Se usa print para incluír automaticamente el salto de línea
                print(l, file=destino)

        # Devolver el apuntador del archivo al inicio
        self.f.seek(0)

    def convertir(self, fun, sep=''):
        """Imprime cada uno de los carácteres del archivo después de aplicarles la
           función dada, con el separador dado"""
        for linea in self.f:
            for c in linea:
                # Imprime cada caracter después de aplicarle la función
                print(fun(c), end=sep)

            # Imprimir cada salto de línea
            print()
        
        # Devolver el apuntador del archivo al inicio
        self.f.seek(0)

    def convertirMayusculas(self):
        """Muestra todo el archivo en mayúsculas"""
        self.convertir(str.upper)

    def convertirMinusculas(self):
        """Muestra todo el archivo en minúsculas"""
        self.convertir(str.lower)

    def convertirHexadecimal(self):
        """Muestra todo el archivo en hexadecimal"""
        self.convertir(lambda c: hex(ord(c))[2:], sep=' ')
