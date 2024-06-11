import random
from PIL import Image
import math 
from cryptography.fernet import Fernet

class Cifrado:
    
    caracter_terminacion = [1, 1, 1, 1, 1, 1, 1, 1]
    
    def __init__(self, clave): 
        self.mensaje : str
        self.token : str
        self.nombreArchivo = str(random.randint(1, 1000))
        self.nombreTxt = "../documentos/"+str(random.randint(1, 1000))+".txt"
        self.rutaOriginal : str
        self.rutaFinal : str
        self.clave = clave
        
        
    
    def cifrar(self, texto):
        key = self.clave
        print(key)
        
        f = Fernet(key.encode())
        self.token = f.encrypt(texto.encode()).decode()


    def obtener_representacion_ascii(self,caracter):
        return ord(caracter)

    def obtener_representacion_binaria(self,numero):
        return bin(numero)[2:].zfill(8)

    def cambiar_ultimo_bit(self,byte, nuevo_bit):
        return byte[:-1] + str(nuevo_bit)

    def binario_a_decimal(self,binario):
        return int(binario, 2)

    def modificar_color(self, color_original, bit):
        color_binario = self.obtener_representacion_binaria(color_original)
        color_modificado = self.cambiar_ultimo_bit(color_binario, bit)
        return self.binario_a_decimal(color_modificado)

    def obtener_lista_de_bits(self, texto):
        lista = []
        for letra in texto:
            representacion_ascii = self.obtener_representacion_ascii(letra)
            representacion_binaria = self.obtener_representacion_binaria(representacion_ascii)
            for bit in representacion_binaria:
                lista.append(bit)
        for bit in self.caracter_terminacion:
            lista.append(bit)
        return lista

    def ocultarMensaje(self, mensaje, ruta_imagen_original):
        self.crearTxt(mensaje)
        self.cifrar(mensaje)
        self.mensaje = mensaje
        ruta_imagen_salida = self.nombreArchivo+".png"
        print("Ocultando mensaje...".format(mensaje))
        self.rutaOriginal = ruta_imagen_original
        self.rutaFinal = "../logica/imagenes/"+ruta_imagen_salida
        imagen = Image.open(ruta_imagen_original)
        pixeles = imagen.load()

        tamaño = imagen.size
        
        anchura = tamaño[0]
        altura = tamaño[1]
        if anchura<=1024 and altura<=768:
            print("Tamaño de la imagen correcto")
        else:
            print("Tamaña demasiado grando")
            return 0
            
        
        
        lista = self.obtener_lista_de_bits(self.token)
        contador = 0
        longitud = len(lista)
        for x in range(anchura):
            for y in range(altura):
                if contador < longitud:
                    pixel = pixeles[x, y]


                    rojo = pixel[0]
                    verde = pixel[1]
                    azul = pixel[2]

                    if contador < longitud:
                        rojo_modificado = self.modificar_color(rojo, lista[contador])
                        contador += 1
                    else:
                        rojo_modificado = rojo

                    if contador < longitud:
                        verde_modificado = self.modificar_color(verde, lista[contador])
                        contador += 1
                    else:
                        verde_modificado = verde

                    if contador < longitud:
                        azul_modificado = self.modificar_color(azul, lista[contador])
                        contador += 1
                    else:
                        azul_modificado = azul

                    pixeles[x, y] = (rojo_modificado, verde_modificado, azul_modificado)
                else:
                    break
            else:
                continue
            break

        if contador >= longitud:
            print("Mensaje escrito correctamente")
        else:
            print("Advertencia: no se pudo escribir todo el mensaje, sobraron {} caracteres".format( math.floor((longitud - contador) / 8) ))

        imagen.save(self.rutaFinal)
    
    def crearTxt(self, mensaje):
        try:
            with open(self.nombreTxt, "w") as archivo:
                archivo.write(mensaje)
            archivo.close()
        except Exception as e:
            print("Ha ocurrido un error en el guardado del texto")


    



    

