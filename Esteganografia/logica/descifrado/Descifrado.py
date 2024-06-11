from PIL import Image
from cryptography.fernet import Fernet
 

class Descifrado:
    
    caracter_terminacion = "11111111"
    
    def __init__(self, clave):
        self.clave = clave
        self.token = ""
        self.ruta= ""
        self.mensaje = ""
        
    def descifrar(self):
        try:
            f = Fernet(self.clave)
            self.mensaje = f.decrypt(self.token).decode()
            print(self.mensaje)
        except Exception as e:
            print(e)
    
    def obtener_lsb(self,byte):
        return byte[-1]

    def obtener_representacion_binaria(self,numero):
        return bin(numero)[2:].zfill(8)

    def binario_a_decimal(self,binario):
        return int(binario, 2)

    def caracter_desde_codigo_ascii(self,numero):
        return chr(numero)

    def leer(self,ruta_imagen):
        imagen = Image.open(self.ruta+ruta_imagen)
        pixeles = imagen.load()

        tamaño = imagen.size
        anchura = tamaño[0]
        altura = tamaño[1]

        byte = ""

        for x in range(anchura):
            for y in range(altura):
                pixel = pixeles[x, y]

                rojo = pixel[0]
                verde = pixel[1]
                azul = pixel[2]


                byte += self.obtener_lsb(self.obtener_representacion_binaria(rojo))
                if len(byte) >= 8:
                    if byte == self.caracter_terminacion:
                        break
                    self.token += self.caracter_desde_codigo_ascii(self.binario_a_decimal(byte))
                    byte = ""

                byte += self.obtener_lsb(self.obtener_representacion_binaria(verde))
                if len(byte) >= 8:
                    if byte == self.caracter_terminacion:
                        break
                    self.token += self.caracter_desde_codigo_ascii(self.binario_a_decimal(byte))
                    byte = ""

                byte += self.obtener_lsb(self.obtener_representacion_binaria(azul))
                if len(byte) >= 8:
                    if byte == self.caracter_terminacion:
                        break
                    self.token += self.caracter_desde_codigo_ascii(self.binario_a_decimal(byte))
                    byte = ""

            else:
                continue
            break
        print("El mensaje oculto es:")
        print(self.token)
        self.descifrar()
    



