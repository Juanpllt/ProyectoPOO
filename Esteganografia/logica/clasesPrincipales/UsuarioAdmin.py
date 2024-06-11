import sys
sys.path.append("../../")
from logica.clasesPrincipales.Usuario import Usuario

class UsuarioAdmin(Usuario):
    
    def __init__(self, id,  nombreUsuario, nombre, contrasena, correo, documento, rol=2):
        super().__init__(id, nombreUsuario, nombre, contrasena, correo, documento, rol)
    
    
