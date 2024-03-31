from Usuario import Usuario

class UsuarioAdmin(Usuario):
    
    def __init__(self, nombreUsuario="", nombre="", contrasena="", correo="", documento=""):
        super().__init__(nombreUsuario, nombre, contrasena, correo, documento)
    
    def verUsuarios(self):
        pass
    def descargarUsos(self):
        pass
    def buscarUsuarios(self):
        pass
    def borrarUsuario(self):
        pass
    #--------------------------
    
    def crearUsuario(self):
        pass
    
    def recuperarContrasena(self):
        pass
    
    