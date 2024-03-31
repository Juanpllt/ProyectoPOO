from Usuario import Usuario

class UsuarioFinal(Usuario):
    
    def __init__(self, nombreUsuario="", nombre="", contrasena="", correo="", documento=""):
        super().__init__(nombreUsuario, nombre, contrasena, correo, documento)
    
    def crearUsuario(self):
        pass
    
    def iniciarSesion(self):
        pass
    
    def recuperarContrasena(self):
        pass


usuario = UsuarioFinal("Jupa", "juan", "nexxuz","juan@gmail.com","1040872055")

