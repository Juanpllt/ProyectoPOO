import sys
sys.path.append("../../")
from logica.clasesPrincipales.Clave import Clave
from logica.cifrado.Cifrado import Cifrado
from logica.descifrado.Descifrado import Descifrado
from persistencia.ControladorClavePersistencia import ControladorClavePersistencia


class ControladorEsteganografia:
    
    
    
    def __init__(self, idUsuario):
        self.controladorClavePersistencia = ControladorClavePersistencia()
        self.clave = Clave()
        self.idUsuario = idUsuario
        self.verClave()
        
        print(self.clave.clave)
    
    def verClave(self):
        key = self.controladorClavePersistencia.verClave()
        self.clave.clave = key[1]
    
    def cambiarClave(self, id=1):
        
        self.clave.crearClave()
        clave = self.clave.clave[1]
        self.controladorClavePersistencia.cambiarClave(str(clave), id)
    
    def ingresarPrimerClave(self, id=1):
        self.clave.crearClave()
        
        self.controladorClavePersistencia.ingresarClave(self.clave.clave, id)
            
    def eliminarClave(self, id=1):
        self.controladorClavePersistencia.eliminarClave(id)

    
    def cifrar(self, mensaje, ruta):
        try:
            cifrado = Cifrado( self.clave.clave)
            cifrado.ocultarMensaje(mensaje, ruta)
            self.controladorClavePersistencia.crearUsoSoftware(self.idUsuario)
            self.controladorClavePersistencia.hacerEsteganografia(self.idUsuario, cifrado.rutaOriginal,cifrado.rutaFinal, cifrado.nombreTxt)
        except Exception as e:
            print("Ha ocurrido un error en el cifrado",e)
        
    def descifrar(self, ruta):
        try:
            descifrado = Descifrado(self.clave.clave)
            descifrado.leer(ruta)
            self.controladorClavePersistencia.crearUsoSoftware(self.idUsuario)
            return descifrado.mensaje
        except Exception as e:
            print("Ha ocurrido un error en el descifrado", e)







