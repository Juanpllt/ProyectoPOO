import sys
sys.path.append("../../")
from logica.clasesPrincipales.UsuarioAdmin import UsuarioAdmin
from persistencia.ControladorAdminPersistencia import ControladorAdminPersistencia 
from logica.clasesPrincipales.UsuarioFinal import UsuarioFinal
from persistencia.ControladorGeneralPersistencia import ControladorGeneralPersistencia
from persistencia.ControladorClavePersistencia import ControladorClavePersistencia
from typing import Any
import csv

class ControladorUsuarios:
    
    
    codigo = "esteganografia"
    admin : Any = 0
    usuarioFinal : Any = 0
    controladorAdminPersistencia = ControladorAdminPersistencia()
    controladorGeneralPersistencia = ControladorGeneralPersistencia()

    
    def registrarUsuario(self, codigo, nombre, correo, nombreUsuario, documento, contrasena):
        try:
            if codigo == self.codigo:
                rol = 2
                self.controladorAdminPersistencia.crearUsuario(nombre, correo, nombreUsuario, rol, documento, contrasena)
                
            elif codigo == "1":
                rol = 1
                self.controladorGeneralPersistencia.crearUsuario(nombre, correo, nombreUsuario, rol, documento, contrasena)
                
            else:
                print("El codigo es el incorrecto")
        except Exception as e:
            print("Ha ocurrido un error ControladoUsuarios",e)
    
    
    def iniciarSesion(self, nombreUsuario, contrasena):
        try:
            usuario = self.controladorGeneralPersistencia.consultarUsuario(nombreUsuario, contrasena)
            if usuario[4]==1:
                self.usuarioFinal = UsuarioFinal(usuario[0], usuario[3], usuario[1], usuario[6],usuario[2], usuario[5])
                return self.usuarioFinal
            elif usuario[4]==2:
                self.admin = UsuarioAdmin(usuario[0], usuario[3], usuario[1], usuario[6],usuario[2], usuario[5])
                return self.admin
            else:
                print("No cumple con los roles")
                
        except Exception as e:
            print("Ha ocurrido un error",e)
    def consultarUsoSoftware(self):
        try:
            with open("C:/Users/juanp/Documentos/ProyectoEsteganografia/Esteganografia/logica/documentos/Usos.csv", "w") as archivo:
                writer = csv.writer(archivo)
                usos = ControladorClavePersistencia().consultarUsoSoftware()
                for uso in usos:
                    writer.writerow(uso)
        except Exception as e:
            print("Error",e)
    
    def consultarEsteganografia(self):
        try:
            with open("C:/Users/juanp/Documentos/ProyectoEsteganografia/Esteganografia/logica/documentos/Esteganografia.csv", "w") as archivo:
                writer = csv.writer(archivo)
                usos = ControladorClavePersistencia().consultarEsteganografia()
                for uso in usos:
                    writer.writerow(uso)
        except Exception as e:
            print("Error",e)
    
    def consultarUsuarios(self):
        try:
            with open("C:/Users/juanp/Documentos/ProyectoEsteganografia/Esteganografia/logica/documentos/Usuarios.csv", "w") as archivo:
                writer = csv.writer(archivo)
                usos = ControladorGeneralPersistencia().consultarUsuarios()
                for uso in usos:
                    writer.writerow(uso)

        except Exception as e:
            print("Error",e)
    def recuperarContrasena(self):
        pass