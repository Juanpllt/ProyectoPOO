import psycopg2
from Conexion import Conexion

class ControladorClavePersistencia:
    
    conexion = Conexion("bubble.db.elephantsql.com", 5432, "kjvgttho", "ltm-xd9v1tZRvF2CwG_1zFX93xnfij6H", "kjvgttho")
    conexionExitosa = conexion.conectar()
    
    def __init__(self) -> None:
        pass
    
    def cambiarClave(self, clave):
        pass 
    