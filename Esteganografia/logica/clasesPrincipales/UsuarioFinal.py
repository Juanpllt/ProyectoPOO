import sys
sys.path.append("../../")
from logica.clasesPrincipales.Usuario import Usuario

class UsuarioFinal(Usuario):
    
    def __init__(self,id,  nombreUsuario, nombre, contrasena, correo, documento, rol=1):
        super().__init__(id, nombreUsuario, nombre, contrasena, correo, documento, rol)
    



